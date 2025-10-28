# faceapi-flask
Face App — Detecção, Landmarks, Expressões, Reconhecimento e Idade/Gênero (face-api.js + Flask)

Aplicação web simples que usa face-api.js (TensorFlow.js) no frontend e Flask no backend para:

 - Detectar rostos em tempo real via webcam

 - Desenhar landmarks e caixas de detecção

 - Estimar expressões faciais

 - Fazer reconhecimento de pessoas (enroll por imagens ou snapshot da webcam)

 - Estimar idade e gênero

Tudo é desenhado em um único <canvas>, evitando problemas de overlay/z-index. O <video> fica fora do DOM e serve apenas como fonte dos frames.

🧱 Arquitetura

Frontend

face-api.js (via CDN) para detecção/landmarks/expressões/reconhecimento/idade-gênero

Canvas único para renderizar frame da webcam + overlays

Enroll de pessoas com LabeledFaceDescriptors + FaceMatcher

Backend

Flask serve os arquivos estáticos e o HTML

Não há processamento de imagem no servidor

📦 Requisitos

Python 3.9+

Node não é necessário (usamos face-api via CDN)

Navegador com suporte a getUserMedia (Chrome, Edge, etc.)

▶️ Executando
python app.py


Acesse: http://127.0.0.1:5000
 (ou http://localhost:5000
).

Passos na UI:

Carregar modelos (CDN por padrão).

Iniciar Webcam.

(Opcional) Cadastrar pessoas (por imagens ou snapshot da webcam) para habilitar reconhecimento.

Ative/desative Landmarks, Expressões, Reconhecimento, Idade/Gênero.

📁 Estrutura do Projeto


├── app.py

├── requirements.txt

├── static

│   └── css

│       └── styles.css

└── templates

    └── index.html


Se quiser usar modelos locais, crie também:

static/

└── models/

    ├── tiny_face_detector_model-weights_manifest.json
    
    ├── tiny_face_detector_model-shard1.bin
    
    ├── ssd_mobilenetv1_model-weights_manifest.json
    
    ├── ssd_mobilenetv1_model-shard1.bin
    
    ├── ssd_mobilenetv1_model-shard2.bin
    
    ├── face_landmark_68_model-weights_manifest.json
    
    ├── face_landmark_68_model-shard1.bin
    
    ├── face_expression_model-weights_manifest.json
    
    ├── face_expression_model-shard1.bin
    
    ├── face_recognition_model-weights_manifest.json
    
    ├── face_recognition_model-shard1.bin
    
    ├── face_recognition_model-shard2.bin
    
    ├── age_gender_model-weights_manifest.json
    
    └── age_gender_model-shard1.bin
    


No app, selecione “Local (/static/models)” antes de carregar os modelos.

🌐 Modelos (CDN vs Local)

CDN (padrão): mais simples; a página baixa os pesos no primeiro uso.

Local: útil em ambientes sem internet. Baixe os arquivos e coloque em static/models/, então troque para Local e clique Carregar modelos.

🧭 Reconhecimento de Rosto

Cadastrar por imagens: selecione uma ou mais fotos de uma pessoa, informe o nome e clique “Cadastrar das imagens”.

Cadastrar pela webcam: informe o nome, inicie a webcam, clique “Cadastrar da webcam” (faz snapshot do frame atual).

Ajuste o limiar (threshold) conforme necessário (0.50–0.60 normalmente é bom).

⚙️ Configurações úteis

Detector:

SSD Mobilenet → melhor qualidade (padrão).

Tiny → mais rápido; ajuste inputSize (ex.: 320/384) e score.

Idade/Gênero: a idade tem suavização por EMA (exponencial), evitando mudanças bruscas.

🧪 Dicas de Performance

Iluminação frontal ajuda muito na detecção e reconhecimento.

Em máquinas modestas, use Tiny com inputSize=320 para manter FPS.

Desligue Landmarks e Expressões se só precisar de reconhecimento.

🔐 Segurança & Privacidade

Todo o processamento de vídeo/rosto acontece no navegador.

O servidor Flask só entrega arquivos estáticos/HTML.

Não há armazenamento de imagens no backend. (Os descritores de “enroll” vivem na memória do navegador enquanto a página está aberta.)

🙏 Créditos

face-api.js (por @justadudewhohacks e colaboradores)

TensorFlow.js

Flask
