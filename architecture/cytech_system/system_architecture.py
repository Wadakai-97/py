from diagrams import Diagram, Cluster, Edge
from diagrams.aws.compute import EC2, EKS
from diagrams.aws.database import RDS, Redshift
from diagrams.aws.network import APIGateway, ELB, Route53, VPC, NATGateway, InternetGateway
from diagrams.aws.security import Cognito, IAM
from diagrams.aws.analytics import Glue
from diagrams.aws.ml import Sagemaker
from diagrams.aws.management import Cloudwatch, Cloudtrail
from diagrams.aws.integration import SQS
from diagrams.aws.storage import S3
from diagrams.generic.device import Mobile
from diagrams.generic.compute import Rack
from diagrams.onprem.client import User
from diagrams.onprem.vcs import Github
from diagrams.onprem.ci import Jenkins
from diagrams.programming.language import Python

# システムアーキテクチャ図の作成
with Diagram("CyTech Adaptive Design System Architecture", show=True, filename="optimized_architecture", direction="LR"):
    
    # ユーザー & 認証
    user = User("Web User")
    mobile = Mobile("Mobile User")
    auth = Cognito("AWS Cognito / Auth0")

    # ネットワーク & セキュリティ
    with Cluster("Networking & Security"):
        route53 = Route53("Route 53 (DNS)")
        vpc = VPC("VPC")
        internet_gateway = InternetGateway("Internet Gateway")
        nat_gateway = NATGateway("NAT Gateway")
        security = IAM("IAM Policies & Roles")

    # パブリックサブネット
    with Cluster("Public Subnet"):
        elb = ELB("Elastic Load Balancer")
        api_gateway = APIGateway("API Gateway")

    # プライベートサブネット（アプリ & コンテナ）
    with Cluster("Private Subnet (Applications)"):
        with Cluster("Application Layer"):
            superblocks = Python("Superblocks (Low-Code Platform)")
            backend = EC2("Backend (Go / Laravel / Flutter)")
        
        with Cluster("Container Orchestration"):
            eks = EKS("EKS Cluster")

    # データベース
    with Cluster("Database Layer (Private Subnet)"):
        db = RDS("Amazon RDS (MySQL / PostgreSQL)")
        db_access = IAM("DB Access Control")  

    # ETL 処理
    with Cluster("ETL Processing"):
        etl = Glue("AWS Glue / Apache Airflow / dbt")

    # データウェアハウス
    with Cluster("Data Warehouse"):
        dwh = Redshift("Amazon Redshift / Snowflake / BigQuery")

    # CI/CD パイプライン
    with Cluster("CI/CD Pipeline"):
        github = Github("GitHub Repository")
        jenkins = Jenkins("Jenkins CI/CD")
        codepipeline = Rack("AWS CodePipeline")  
        codebuild = Rack("AWS CodeBuild")  
        codedeploy = Rack("AWS CodeDeploy")  

    # ストレージ & メッセージキュー
    with Cluster("Storage & Queueing"):
        storage = S3("S3 Buckets")
        queue = SQS("Message Queue (SQS)")

    # BI & 分析ツール
    with Cluster("BI & Analytics"):
        bi_tool = Sagemaker("BI & Data Visualization")

    # 監視とロギング
    with Cluster("Monitoring & Logging"):
        monitoring = Cloudwatch("CloudWatch / OpenTelemetry")
        logging = Cloudtrail("AWS CloudTrail")

    # ユーザーの認証フロー
    user >> Edge(label="Login (OAuth 2.0 / OIDC)") >> auth >> Edge(label="Issue Token") >> api_gateway
    mobile >> Edge(label="Login (OAuth 2.0 / OIDC)") >> auth >> Edge(label="Issue Token") >> api_gateway

    # ネットワークの流れ
    route53 >> Edge(label="DNS Resolution") >> internet_gateway
    internet_gateway >> Edge(label="Public Traffic Routing") >> elb
    elb >> Edge(label="Load Balancing") >> api_gateway

    # API Gateway のルーティング
    api_gateway >> Edge(label="Forward Requests") >> superblocks
    api_gateway >> Edge(label="Forward Requests") >> backend

    # データ保存
    superblocks >> Edge(label="Write Data") >> db
    backend >> Edge(label="Write Data") >> db
    db >> Edge(label="Access Control") >> db_access  

    # ETL 処理
    db >> Edge(label="Extract Data") >> etl
    etl >> Edge(label="Transform & Load") >> dwh

    # DWH クエリ
    api_gateway >> Edge(label="Query Data") >> dwh
    superblocks >> Edge(label="Query Data") >> dwh
    backend >> Edge(label="Query Data") >> dwh

    # BI ツールへのデータ提供
    dwh >> Edge(label="Analyze & Visualize") >> bi_tool

    # CI/CD ワークフロー
    github >> Edge(label="Push Code") >> jenkins
    jenkins >> Edge(label="Trigger Pipeline") >> codepipeline
    codepipeline >> Edge(label="Build Code") >> codebuild
    codebuild >> Edge(label="Deploy to Infrastructure") >> codedeploy
    codedeploy >> Edge(label="Update Backend") >> backend

    # セキュリティ管理
    security >> Edge(label="IAM Policy Enforcement") >> backend
    security >> Edge(label="DB Access Control") >> db_access  

    # メッセージキュー統合
    backend >> Edge(label="Queue Messages") >> queue
    queue >> Edge(label="Process Tasks") >> backend

    # 監視・ロギング
    api_gateway >> Edge(label="Log API Calls") >> monitoring
    db >> Edge(label="Monitor Queries") >> monitoring
    dwh >> Edge(label="Track Usage") >> monitoring
    backend >> Edge(label="Log Application Events") >> logging
    codedeploy >> Edge(label="Track Deployment Logs") >> logging
    monitoring >> Edge(label="Alert on Anomalies") >> logging
