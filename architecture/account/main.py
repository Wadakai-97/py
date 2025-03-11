from diagrams import Diagram, Cluster
from diagrams.aws.compute import Lambda
from diagrams.aws.database import RDS, Dynamodb, ElastiCache
from diagrams.aws.network import APIGateway, CloudFront
from diagrams.aws.security import WAF, IAM
from diagrams.aws.management import Cloudwatch
from diagrams.aws.integration import SQS, Eventbridge
from diagrams.aws.storage import S3
from diagrams.aws.general import User

def create_authentication_layer():
    user = User("End User")
    cognito = IAM("AWS Cognito\n(認証管理)")
    return user, cognito

def create_authorization_layer():
    with Cluster("API Gateway & Unified API"):
        api_gateway = APIGateway("API Gateway")
        lambda_auth = Lambda("Lambda Authorizer\n(JWT認証)")
        unified_api = Lambda("Unified API\n(統合リクエスト管理)")
    return api_gateway, lambda_auth, unified_api

def create_user_management():
    with Cluster("User Management"):
        user_api = Lambda("User API\n(ユーザー管理)")
        dynamodb = Dynamodb("DynamoDB\n(ユーザー情報)")
    return user_api, dynamodb

def create_microservices():
    with Cluster("Microservices"):
        ct_engineer_service = Lambda("CyTech Engineer API")
        ct_matching_service = Lambda("CyTech Matching API")
        ai_service = Lambda("AI要件定義 API")
    return ct_engineer_service, ct_matching_service, ai_service

def create_data_layer():
    with Cluster("Data Layer"):
        with Cluster("Databases"):
            rds_proxy = RDS("RDS Proxy\n(接続最適化)")
            rds = RDS("Aurora MySQL\n(業務データ)")
        redis = ElastiCache("ElastiCache\n(キャッシュ管理)")
    return rds_proxy, rds, redis

def create_event_driven_services():
    with Cluster("Event-Driven Services"):
        sqs = SQS("SQS\n(非同期処理)")
        kafka = Eventbridge("Kafka/EventBridge\n(リアルタイムデータ同期)")
    return sqs, kafka

def create_monitoring_and_security():
    with Cluster("Monitoring & Security"):
        waf = WAF("AWS WAF\n(攻撃防御)")
        cloudfront = CloudFront("CloudFront\n(CDN)")
        cloudwatch = Cloudwatch("CloudWatch\n(ログ監視)")
    return waf, cloudfront, cloudwatch

def create_storage_layer():
    with Cluster("Storage Layer"):
        s3 = S3("Amazon S3\n(静的コンテンツ)")
    return s3

# AWS インフラ構成図（視認性最適化 + 横長構成）
with Diagram("CyTech Infra Architecture", show=False, direction="LR"):
    user, cognito = create_authentication_layer()
    api_gateway, lambda_auth, unified_api = create_authorization_layer()
    user_api, dynamodb = create_user_management()
    ct_engineer_service, ct_matching_service, ai_service = create_microservices()
    rds_proxy, rds, redis = create_data_layer()
    sqs, kafka = create_event_driven_services()
    waf, cloudfront, cloudwatch = create_monitoring_and_security()
    s3 = create_storage_layer()

    # 認証と認可のフロー
    user >> cognito >> api_gateway >> lambda_auth >> unified_api

    # ユーザー管理API
    unified_api >> user_api >> dynamodb

    # マイクロサービスへのルーティング
    unified_api >> [ct_engineer_service, ct_matching_service, ai_service]

    # データベースアクセス
    [ct_engineer_service, ct_matching_service, ai_service] >> rds_proxy >> rds

    # キャッシュ参照
    unified_api >> redis

    # イベント駆動型データ連携
    dynamodb >> sqs
    dynamodb >> kafka
    kafka >> redis
    sqs >> redis

    # 監視とセキュリティ
    unified_api >> cloudwatch
    cloudfront >> waf >> api_gateway

    # 静的コンテンツ配信
    s3 >> cloudfront
