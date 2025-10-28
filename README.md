# faceapi-flask
Face App — Detecção, Landmarks, Expressões, Reconhecimento e Idade/Gênero (face-api.js + Flask)

Aplicação web simples que usa face-api.js (TensorFlow.js) no frontend e Flask no backend para:

 - Detectar rostos em tempo real via webcam

 - Desenhar landmarks e caixas de detecção

 - Estimar expressões faciais

 - Fazer reconhecimento de pessoas (enroll por imagens ou snapshot da webcam)

 - Estimar idade e gênero

Tudo é desenhado em um único <canvas>, evitando problemas de overlay/z-index. O <video> fica fora do DOM e serve apenas como fonte dos frames.
