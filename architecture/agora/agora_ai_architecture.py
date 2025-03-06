from diagrams import Diagram, Cluster, Edge
from diagrams.aws.ml import Transcribe, Polly
from diagrams.custom import Custom
from diagrams.onprem.compute import Server
from diagrams.onprem.client import User
from diagrams.onprem.network import Nginx
from diagrams.onprem.inmemory import Redis
from diagrams.aws.compute import Lambda
from diagrams.onprem.container import Docker
from diagrams.aws.analytics import Kinesis
from diagrams.aws.devtools import Codebuild

# Define a function to create custom icons within the Diagram context
def create_custom_icon(name, url):
    return Custom(name, url)

# Use custom icons for Agora since it's not available in diagrams package
agora_icon_url = "https://upload.wikimedia.org/wikipedia/commons/8/84/Agora.io_logo.svg"
webrtc_icon_url = "https://upload.wikimedia.org/wikipedia/commons/6/6c/WebRTC_logo.svg"
gpt_icon_url = "https://upload.wikimedia.org/wikipedia/commons/4/4a/OpenAI_Logo.svg"

with Diagram("Real-time AI Conversation System", show=True, direction="LR") as diag:
    # Use custom icons where necessary
    agora_node = create_custom_icon("Agora RTC", agora_icon_url)
    webrtc_node = create_custom_icon("WebRTC", webrtc_icon_url)
    gpt_node = create_custom_icon("OpenAI GPT-4", gpt_icon_url)
    audio_stream_node = create_custom_icon("Live Audio", "https://upload.wikimedia.org/wikipedia/commons/d/d7/Sound-icon.svg")
    
    user = User("User")
    
    with Cluster("Real-time Processing\n(Capturing Audio & Video)"):
        user >> Edge(label="Speaks / Streams") >> audio_stream_node
        audio_stream_node >> Edge(label="Processed by Agora") >> agora_node
        agora_node >> Edge(label="Transfers data via WebRTC") >> webrtc_node
    
    with Cluster("AI Processing\n(Speech Recognition & Response Generation)"):
        transcribe_node = Transcribe("Speech-to-Text API")
        polly_node = Polly("Text-to-Speech API")
        
        webrtc_node >> Edge(label="Sends Audio Data") >> transcribe_node
        transcribe_node >> Edge(label="Converts to Text") >> gpt_node
        gpt_node >> Edge(label="Generates Response") >> polly_node
    
    with Cluster("Backend\n(Data Handling & Storage)"):
        websocket_server = Nginx("WebSockets for Sync")
        cache = Redis("Session Cache")
        lambda_backend = Lambda("AI Processing Backend")
        
        gpt_node >> Edge(label="Sends Response") >> lambda_backend
        lambda_backend >> Edge(label="Stores Data") >> cache
        websocket_server >> Edge(label="Syncs Response") >> lambda_backend
    
    with Cluster("Frontend & UI\n(User Interaction)"):
        frontend_ui = Server("Flutter Web / React UI")
        
        frontend_ui >> Edge(label="Receives Response") >> websocket_server
        frontend_ui >> Edge(label="Displays UI Updates") >> user
    
    polly_node >> Edge(label="Converts to Speech") >> agora_node
    agora_node >> Edge(label="Delivers Audio Response") >> user