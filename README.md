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
