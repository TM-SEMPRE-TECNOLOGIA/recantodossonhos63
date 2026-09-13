# -*- coding: utf-8 -*-
import os

paths = [
    r'site-recanto-dos-sonhos\assets\images\rancho',
    r'C:\Users\mikaa\Downloads\FOTOS DO RANCHO\ORGANIZADAS_POR_SECAO'
]

prompts_data = {
    '01-hero-e-aereas': {
        'drone-ilha-areia-araguaia-4k.jpg': {
            'tipo': 'Color Grading / Upscale / Realce Fotográfico (SEM IA GENERATIVA PLÁSTICA)',
            'o_que_manter': 'Manter 100% da geografia real: o banco de areia exato, a vegetação ciliar nativa, a transparência verde-esmeralda da água e as tendas reais montadas.',
            'o_que_ajustar': 'Realçar a nitidez dos detalhes da areia submersa e da correnteza. Aumentar levemente o contraste e a saturação natural das cores quentes da areia e do verde da floresta. Sem aspecto de maquete ou render.',
            'prompt_en': 'Editorial drone landscape photography of the Araguaia River sand island in Tocantins Brazil, crystalline emerald green water with natural shallow sand ripples, deep lush riparian forest, bright natural sunlight, genuine aerial camera photograph, DJI Mavic 3 Pro Cine 4K raw, realistic natural color grade, subtle micro-contrast, zero CGI, zero 3D render, uncompressed authentic textures.',
            'prompt_pt': 'Fotografia aérea editorial com drone do banco de areia no Rio Araguaia, Peixe Tocantins. Água cristalina com tons esmeralda naturais revelando ondulações de areia rasa, mata ciliar densa e preservada, luz solar natural sem exagero. Textura de foto real de alta resolução, zero efeito plástico de render 3D, zero aspecto artificial.'
        },
        'drone-por-do-sol-rancho-mata.jpg': {
            'tipo': 'Realce de Iluminação / Dynamic Range / Pôr do Sol',
            'o_que_manter': 'A estrutura real do rancho em meio à mata, a estrada de terra que leva até a margem do Rio Araguaia e a silhueta da ilha ao fundo.',
            'o_que_ajustar': 'Recuperar detalhes nas sombras da copa das árvores (sem ruído digital) e intensificar a luz dourada (golden hour) refletida no espelho de água do rio.',
            'prompt_en': 'Atmospheric aerial photograph of a rustic riverside eco-lodge nestled in thick Brazilian Cerrado woodland, dirt path leading to the vast Araguaia River, warm golden hour sunset glowing on the horizon and reflecting on the water surface, soft natural shadows, authentic 35mm filmic lighting, documentary aerial shot, no CGI smoothing, organic tree canopy details, natural lens bloom.',
            'prompt_pt': 'Fotografia aérea do rancho ecológico no cerrado tocantinense à beira do Rio Araguaia. Pôr do sol dourado refletindo na água, estrada de terra entre a mata nativa. Recuperação suave de sombras nas árvores, luz quente natural de fim de tarde, sem renderização artificial de IA, texturas reais de folhas e terra.'
        },
        'por-do-sol-rio-araguaia.jpg': {
            'tipo': 'Ajuste de Luz / Silhueta Natural',
            'o_que_manter': 'A imensidão do rio e a linha do horizonte com as margens da mata.',
            'o_que_ajustar': 'Aumentar a faixa dinâmica dos reflexos dourados na água e o gradiente do céu ao pôr do sol, mantendo o grão fotográfico natural.',
            'prompt_en': 'Authentic golden hour sunset photograph directly over the calm Araguaia river, vibrant warm amber and gold light reflection across water ripples, silhouette of distant riverbank forest, analog camera look, 50mm f/4, natural exposure, organic film grain, zero artificial glow, realistic documentary nature shot.',
            'prompt_pt': 'Foto real de pôr do sol sobre as águas calmas do Rio Araguaia. Reflexo âmbar e dourado nas ondulações da água, silhueta da mata nas margens, estética fotográfica natural com leve textura de filme, sem pós-processamento artificial.'
        }
    },
    '02-praia-e-barcos': {
        'barcos-voadeiras-recanto-dos-sonhos.jpg': {
            'tipo': 'Inpainting / Limpeza de Timestamp / Realce de Textura',
            'o_que_manter': 'CRUCIAL: Manter os 3 barcos de alumínio idênticos, especialmente o barco central com o adesivo real escrito "Recanto dos Sonhos" e o motor de popa Mercury. Manter os banhistas ao fundo na água.',
            'o_que_ajustar': 'REMOVER OBRIGATORIAMENTE o texto de timestamp ("17 de maio de 2026 15:06") no canto inferior esquerdo. Realçar o reflexo límpido na beira da praia e a textura do alumínio.',
            'prompt_en': 'Professional hospitality documentary photography, three rustic aluminum river skiff boats moored on the golden sandbank shoreline of Araguaia river, authentic boat hull clearly displaying the decal "Recanto dos Sonhos", black outboard Mercury motor, clear river water gently lapping the sand, people swimming in background, sunny Brazilian afternoon, sharp realistic photography, remove date stamp watermark, preserve all boat details, realistic sand grains, no AI gloss, authentic camera capture.',
            'prompt_pt': 'Foto documental realista dos três barcos de alumínio ancorados na areia dourada do Rio Araguaia. Preservar o adesivo real escrito "Recanto dos Sonhos" e os motores Mercury. Remover completamente a data e hora do rodapé. Luz natural de tarde ensolarada, texturas reais de areia e metal escovado, zero estética de render 3D.'
        },
        'tenda-privativa-praia-araguaia-01.jpg': {
            'tipo': 'Inpainting / Remoção de Carimbo / Color Grade Realista',
            'o_que_manter': 'A estrutura exata da tenda branca de lona piramidal montada na beira da água, o sombrite preto, o tambor de churrasqueira, as cadeiras laranjas e a escultura de coração no rio.',
            'o_que_ajustar': 'REMOVER OBRIGATORIAMENTE a data ("23 de julho de 2026 8:52 AM") no canto inferior esquerdo. Realçar o azul cristalino do céu e a transparência rasa da água onde a sombra da tenda se projeta.',
            'prompt_en': 'High-end travel editorial photograph of an exclusive white marquee canopy tent set on pristine river beach sand directly at the water edge of Rio Araguaia, orange folding chairs under shade, black fabric side curtain, calm clear freshwater, distant green shore under bright blue sky, remove timestamp watermark, sharp details on sand texture and water clarity, authentic natural photography, no plastic smoothing, Leica SL2 aesthetic.',
            'prompt_pt': 'Fotografia editorial da tenda privativa branca montada na areia da praia do Rio Araguaia, cadeiras de descanso sob a sombra, água rasa e cristalina na margem. Remover a data/hora do rodapé. Tons de areia dourada e céu azul vibrante natural, textura rica de areia e lona, sem render digital falso.'
        },
        'tenda-privativa-praia-araguaia-02.jpg': {
            'tipo': 'Inpainting / Remoção de Carimbo / Enquadramento Aberto',
            'o_que_manter': 'A tenda principal em primeiro plano e as outras tendas ao longe no banco de areia, mostrando a amplitude da praia de rio.',
            'o_que_ajustar': 'REMOVER a data ("23 de julho de 2026 8:52 AM"). Equilibrar as sombras duras do sol da manhã para dar ar convidativo.',
            'prompt_en': 'Wide angle realistic photo of white beach event tents along the vast sandbar of Araguaia river, bright sunny summer day, clear blue water, authentic natural textures of dry and wet sand, remove date timestamp, documentary travel style, natural sun reflections on water, zero digital CGI render.',
            'prompt_pt': 'Foto aberta da praia do Araguaia com a tenda privativa e cadeiras na areia. Remover o carimbo de data. Realce da areia fofa e do contraste natural com a água limpa do rio, preservando o aspecto 100% fotográfico.'
        },
        'rede-dentro-dagua-araguaia.jpg': {
            'tipo': 'Remoção de Carimbo / Denoise / Aumento de Nitidez Natural',
            'o_que_manter': 'A cena real: a rede de descanso deitada dentro da água do rio sustentada por suportes, pessoas relaxando com água até a cintura.',
            'o_que_ajustar': 'REMOVER a data ("22 de julho de 2026 1:27 PM"). A foto original tem ruído de zoom digital; aplicar redução de ruído que preserve a textura da pele e a limpidez da água sem deixar os rostos emborrachados.',
            'prompt_en': 'Documentary style lifestyle photography of people resting comfortably in a hammock hung directly inside shallow clear river waters, refreshing tropical river scene, green forest riverbank in background, remove timestamp watermark, enhance natural clarity of water ripples, preserve authentic human skin textures, no plastic airbrushing, realistic Canon EOS photography.',
            'prompt_pt': 'Cena de lazer com rede montada dentro da água cristalina do Rio Araguaia, pessoas se refrescando. Remover o carimbo de data. Limpeza do ruído digital sem transformar pessoas em bonecos de cera, preservando ondulações naturais da água e a mata ao fundo.'
        }
    },
    '03-estrutura-e-lazer': {
        'piscina-aquecida-deck-azul.jpg': {
            'tipo': 'Equilíbrio de Luz / Realce de Cor / Textura',
            'o_que_manter': 'A piscina redonda elevada com deck azul, a casa com toldo azul ao fundo, a churrasqueira de alvenaria e o gramado verde.',
            'o_que_ajustar': 'Diminuir a dureza das sombras dos galhos das árvores que cruzam a frente da foto. Valorizar a água limpa da piscina e o verde do gramado sem saturação radioativa.',
            'prompt_en': 'Sunny afternoon photograph of a private country lodge backyard, round plunge pool with vibrant blue painted deck surrounded by green grass lawn, rustic outdoor barbecue station and covered veranda in background, native shade trees, softened natural branch shadows, crisp clean water, authentic architectural photography, realistic textures of brick and grass, no 3D CGI.',
            'prompt_pt': 'Fotografia da área externa do rancho com piscina redonda de deck azul no gramado, casa e churrasqueira ao fundo. Suavizar sombras duras dos galhos, realçar a água límpida da piscina e o gramado verde. Estilo fotográfico autêntico, sem acabamento liso de render de arquitetura 3D.'
        },
        'varanda-gourmet-sinuca-piscina.jpg': {
            'tipo': 'Inpainting / Remoção de Carimbo / Iluminação de Sombras',
            'o_que_manter': 'O galpão/varanda com a mesa de sinuca/bilhar à esquerda, o balcão, a piscina e mesa de pedra no gramado ensolarado à direita.',
            'o_que_ajustar': 'REMOVER OBRIGATORIAMENTE a data ("17 de setembro de 2025 10:43"). Clarear o interior sombreado da varanda para a mesa de sinuca ficar bem visível e convidativa.',
            'prompt_en': 'Spacious open-air covered veranda of a Brazilian riverside lodge featuring a classic pool billiard table, seamlessly connected to a sunny green lawn with a round swimming pool and umbrella table, bright daylight outside, balanced fill light inside the porch revealing billiard table details, remove timestamp, authentic hospitality photo, realistic concrete floor and wooden beam textures, zero artificial render.',
            'prompt_pt': 'Foto da varanda gourmet ampla com mesa de bilhar/sinuca bem iluminada, conectada ao gramado ensolarado com a piscina ao fundo. Remover a data do rodapé. Iluminação equilibrada entre a área coberta e o sol lá fora, mantendo texturas reais do piso e da estrutura.'
        },
        'mesa-pedra-guarda-sol-piscina.jpg': {
            'tipo': 'Inpainting / Remoção de Distratores / Limpeza Visual',
            'o_que_manter': 'A mesa redonda e os 4 bancos de concreto/pedra no gramado, e a piscina azul ao fundo.',
            'o_que_ajustar': 'REMOVER a data do rodapé. REMOVER a mangueira preta estendida no gramado. REMOVER o logotipo comercial ("Skol") do guarda-sol amarelo, deixando o tecido liso ou em tom bege/amarelo neutro acolhedor.',
            'prompt_en': 'Cozy outdoor seating area in country lodge garden, round stone table with matching curved concrete benches on fresh green grass, neutral warm canvas patio umbrella (clean, no brand logos), round blue pool in background under dappled tree shade, remove date stamp, remove black garden hose on the lawn, clean realistic photograph, crisp details, natural sunlight, no CGI.',
            'prompt_pt': 'Área de convivência no gramado com mesa e bancos de pedra, guarda-sol em lona amarela neutra (sem logos de cerveja), piscina ao fundo sob sombra das árvores. Remover a mangueira do chão e a data do rodapé. Foto limpa, profissional e 100% realista.'
        },
        'pier-coberto-lancha-embarque.jpg': {
            'tipo': 'Aumento de Contraste / Enquadramento / Foco',
            'o_que_manter': 'A descida do rancho entre as árvores nativas até o píer flutuante coberto e a lancha rápida esportiva ancorada no Rio Araguaia.',
            'o_que_ajustar': 'Aumentar a nitidez da lancha e das águas do rio através da folhagem. Equilibrar o contraluz forte.',
            'prompt_en': 'Documentary travel photo looking down a tree-shaded earthen path toward a covered floating boat dock on the Araguaia river, motorboat moored under metal canopy, glittering sunlit river water in background, realistic forest shade, sharp focus on dock and boat, authentic nature photography, no 3D filter.',
            'prompt_pt': 'Foto autêntica do caminho sombreado descendo para o píer privativo coberto no Rio Araguaia, lancha ancorada pronta para navegação. Melhoria de nitidez e contraste, preservando as folhas secas no chão e a textura natural da mata.'
        },
        'jardim-noturno-iluminado.jpg': {
            'tipo': 'Inpainting / Remoção de Carimbo / Ambientação Noturna',
            'o_que_manter': 'O gramado verde, a mesa de pedra, os vasos de plantas e a iluminação noturna do jardim.',
            'o_que_ajustar': 'REMOVER a data do rodapé ("11 de abril de 2026 18:43"). Suavizar o farol do carro na lateral esquerda, dando ênfase a uma iluminação acolhedora de descanso noturno no rancho.',
            'prompt_en': 'Nighttime photograph of a quiet country lodge garden, lush green lawn illuminated by warm garden lights, circular stone patio table and benches, lush tropical trees against twilight night sky, calm relaxing atmosphere, remove date stamp watermark, realistic nighttime exposure, natural shadows, no artificial neon.',
            'prompt_pt': 'Foto noturna do jardim e gramado do rancho iluminado, mesa de pedra e árvores ao fundo sob o céu crepuscular. Remover o carimbo de data. Luz quente e acolhedora de fim de noite no campo, sem ruído exagerado e sem render falso.'
        },
        'tenda-mesas-sombra.jpg': {
            'tipo': 'Ajuste de Luz / Contraste / Cores',
            'o_que_manter': 'O quiosque/tenda coberta com mesas e cadeiras na área de terra batida sob a copa das árvores.',
            'o_que_ajustar': 'Clarear a área sob a tenda para evidenciar o espaço de descanso sombreado para grandes grupos.',
            'prompt_en': 'Large shaded marquee tent in a rustic wooded clearing, several black outdoor dining tables and chairs arranged for group gatherings, natural sandy ground, sunlight filtering through tall green trees in background, authentic countryside retreat photograph, balanced exposure, natural tones.',
            'prompt_pt': 'Espaço sombreado de convivência sob tenda na mata com mesas e cadeiras para grupos. Clareamento das sombras internas, preservando a rusticidade do chão de terra batida e a luz natural entre as árvores.'
        }
    },
    '04-acomodacoes': {
        'suite-casal-ar-condicionado.jpg': {
            'tipo': 'Interior Design Uplift / Preservação Arquitetônica Estrutural',
            'o_que_manter': 'CRUCIAL: Manter a estrutura EXATA do quarto: cama de casal na mesma posição à esquerda, mesa de apoio/estudo ao centro, parede de fundo salmão/terracota, aparelho de ar-condicionado na parede direita, teto e paredes laterais idênticos.',
            'o_que_ajustar': 'REMOVER o carimbo de data ("17 de maio de 2026 09:53"). Substituir a colcha por um enxoval de algodão acolhedor bem arrumado em tons claros/neutros com travesseiros confortáveis (com dobras naturais de tecido, sem aspecto liso de render). Substituir a cadeira de plástico branca por uma cadeira rústica de madeira clara. Luz natural suave entrando pela porta.',
            'prompt_en': 'Editorial hospitality photo of a neat rustic guest bedroom, comfortable queen bed made with crisp textured beige and white cotton linen with natural soft folds and plush pillows, salmon-terracotta accent wall with framed sunset art, light wooden desk with a simple matching wooden chair, split air conditioning unit on white rustic wall, natural soft morning daylight, cozy and impeccably clean, authentic architectural photography, realistic wood and fabric textures, strictly NO plastic 3D render look, remove timestamp.',
            'prompt_pt': 'Foto de quarto de rancho acolhedor e impecavelmente arrumado. Cama de casal com roupa de cama de algodão bege/branco com dobras e texturas naturais, parede de cabeceira em tom terracota com quadros náuticos, escrivaninha de madeira com cadeira de madeira simples, ar-condicionado na parede. Remover carimbo de data. Iluminação natural aconchegante, mantendo a estrutura original do quarto, zero efeito de render 3D computadorizado.'
        },
        'quarto-familia-duas-camas.jpg': {
            'tipo': 'Interior Design Uplift / Preservação da Estrutura de Madeira/OSB',
            'o_que_manter': 'Manter o layout idêntico: as duas camas box casal lado a lado, as paredes revestidas em painel de OSB/madeira texturizada, o ar-condicionado na parede direita e os quadros náuticos ao fundo.',
            'o_que_ajustar': 'REMOVER a data ("17 de maio de 2026 09:55"). Trocar as roupas de cama simples por lençóis e cobre-leitos coordenados em tons neutros (linho/algodão cru ou verde sálvia suave) com travesseiros arrumados. Adicionar uma iluminação quente e suave (2700K) que destaque a textura rústica da madeira OSB.',
            'prompt_en': 'Warm and inviting rustic lodge family bedroom, two comfortable double beds positioned side by side dressed in high quality natural textured linen quilts and fluffy pillows, walls lined with authentic textured OSB wood panels, trio of nautical wall art, split air conditioner on the right, warm ambient 2700k room lighting, cozy atmosphere, real architectural photography, authentic wood grain and textile micro-textures, zero CGI smoothing, remove date watermark.',
            'prompt_pt': 'Quarto família com duas camas de casal no rancho. Paredes em painel de madeira OSB autêntico com quadros náuticos, ar-condicionado na parede. Camas vestidas com edredons e lençóis aconchegantes em tecido natural com textura real. Iluminação quente e convidativa, preservando 100% da disposição original sem aspecto artificial de maquete 3D. Remover carimbo de data.'
        },
        'quarto-hospedes-cama-casal.jpg': {
            'tipo': 'Inpainting / Remoção de Carimbo / Arrumação Acolhedora',
            'o_que_manter': 'A disposição exata: cama de casal à esquerda, escrivaninha de madeira, parede salmão ao fundo e ar-condicionado na direita.',
            'o_que_ajustar': 'REMOVER a data ("3 de maio de 2026 20:09"). Substituir a cadeira plástica por cadeira de madeira e vestir a cama com roupa de cama arrumada em tons neutros acolhedores.',
            'prompt_en': 'Clean rustic lodge bedroom interior, neatly arranged double bed with warm neutral duvet and pillows, wooden workstation desk, split AC unit, soft warm indoor lamp light, authentic room photo, remove timestamp, real fabric textures, realistic hospitality photography, no artificial AI smoothness.',
            'prompt_pt': 'Quarto de hóspedes com cama de casal arrumada, escrivaninha e ar-condicionado. Remover o carimbo de data. Roupa de cama confortável em tons neutros, iluminação quente aconchegante, mantendo a estrutura real do cômodo.'
        },
        'chales-modulares-externos-01.jpg': {
            'tipo': 'Inpainting / Limpeza de Terreno / Remoção de Carimbo',
            'o_que_manter': 'Os dois chalés modulares externos com estrutura metálica e telhado branco, a árvore central que faz sombra e a mata ao redor.',
            'o_que_ajustar': 'REMOVER a data ("3 de maio de 2026 15:02"). Limpar pequenas folhas soltas e substituir as cadeiras plásticas por banquinhos ou cadeiras de madeira na varandinha dos chalés. Luz solar suave entre os galhos.',
            'prompt_en': 'Two modern modular eco-cabins elevated in a shaded clearing surrounded by native Cerrado trees, white corrugated siding with front porch decks, large central shade tree casting dappled sunlight on the ground, authentic eco-lodge photo, remove date timestamp, clean realistic textures of metal and wood, no plastic render.',
            'prompt_pt': 'Chalés modulares suspensos na mata do rancho com varandinha sob a copa de árvore nativa. Remover o carimbo de data. Realçar a luz natural filtrada pelas folhas, texturas nítidas de metal, madeira e terra, preservando a identidade real da pousada.'
        },
        'chales-modulares-externos-02.jpg': {
            'tipo': 'Inpainting / Remoção de Objeto e Carimbo',
            'o_que_manter': 'Os dois chalés modulares com as portas abertas revelando o interior aconchegante.',
            'o_que_ajustar': 'REMOVER OBRIGATORIAMENTE o rastelo/vassoura vermelha caído no chão no canto inferior esquerdo. REMOVER a data ("3 de maio de 2026 15:04").',
            'prompt_en': 'Exterior view of two rustic modular guest cabins in wooded grove with entrance doors open, shaded natural ground, remove red leaf rake from bottom left ground, remove timestamp watermark, warm sunny afternoon light, natural architectural photography, realistic bark and leaf textures, zero CGI.',
            'prompt_pt': 'Visão externa dos dois chalés modulares na mata com portas abertas. Remover o rastelo vermelho do chão e o carimbo de data. Iluminação natural de tarde ensolarada, aspecto 100% fotográfico.'
        },
        'cozinha-copa-rancho.jpg': {
            'tipo': 'Inpainting / Remoção de Plástico / Valorização Rústica',
            'o_que_manter': 'A mesa grande de madeira rústica maciça no centro, a pia com azulejos, a geladeira e o freezer na cozinha do rancho.',
            'o_que_ajustar': 'REMOVER OBRIGATORIAMENTE o plástico protetor transparente enrolado na mesa, revelando o acabamento nobre da madeira envernizada. Adicionar sobre a mesa uma fruteira rústica ou garrafa de café. REMOVER a data ("27 de abril de 2025 16:23").',
            'prompt_en': 'Spacious rustic kitchen and dining area in a countryside river lodge, beautiful solid wood trestle table in center with visible natural wood grain (remove plastic wrap covering), clean tiled floor, refrigerator, stove, window looking onto green trees, warm welcoming country kitchen atmosphere, remove date stamp, authentic interior photography, real wood textures, no 3D render.',
            'prompt_pt': 'Cozinha rústica do rancho com ampla mesa de madeira maciça envernizada (remover o plástico da mesa e mostrar a textura real da madeira). Remover o carimbo de data. Luz natural agradável pela janela, ar aconchegante de rancho acolhedor.'
        }
    },
    '05-social-e-experiencias': {
        'familia-coracao-recanto-araguaia.jpg': {
            'tipo': 'Realce Fotográfico / Denoise / Luz Natural (PRESERVAR PESSOAS E IDENTIDADE)',
            'o_que_manter': 'CRUCIAL: Manter a família real (pais e filhos com seus rostos e sorrisos autênticos), as camisas de pesca com proteção UV e o portal de coração com o letreiro oficial "@Recanto dos Sonhos 63".',
            'o_que_ajustar': 'NÃO ALTERAR OS ROSTOS. Apenas elevar a transparência das ondulações cristalinas da água e o azul do céu. Realce sutil de nitidez nos olhos e nas camisas.',
            'prompt_en': 'Crisp lifestyle family vacation portrait, happy family standing in waist-deep crystal clear river water inside a decorative heart sculpture with sign "Recanto dos Sonhos 63", bright sunny blue sky, beautiful shimmering water ripples revealing sandy bottom, authentic happy expressions, preserve exact real faces and clothing, high resolution documentary photography, no AI facial distortion, no plastic skin smoothing.',
            'prompt_pt': 'Retrato fotográfico autêntico de família aproveitando as águas cristalinas do Rio Araguaia no portal de coração com a placa @Recanto dos Sonhos 63. Preservar 100% os rostos e roupas originais. Realçar apenas a transparência da água e a vivacidade do sol, sem distorção ou filtro artificial na pele.'
        },
        'grupo-amigos-portal-coracao.jpg': {
            'tipo': 'Color Grading / Realce de Nitidez em Grupo',
            'o_que_manter': 'O grupo grande de pessoas sorrindo dentro da água sob o portal de coração.',
            'o_que_ajustar': 'Equilibrar a exposição do céu e a água transparente com fundo de areia dourada. Preservar a autenticidade e espontaneidade de cada pessoa.',
            'prompt_en': 'Group photo of friends and family enjoying vacation in crystal clear shallow river waters around a heart-shaped monument, bright sun, ripples of clear water over sand, authentic vacation memory, natural color correction, sharp focus, no synthetic smoothing, real documentary photo.',
            'prompt_pt': 'Foto de grupo de amigos e família reunidos dentro da água no Rio Araguaia. Correção de cor natural para destacar a água límpida e a luz do sol, preservando a textura real da foto sem intervenção artificial nos rostos.'
        },
        'pesca-peixes-frescos-tabua.jpg': {
            'tipo': 'Fotografia Culinária / Gastronomia Rústica',
            'o_que_manter': 'Os peixes de rio frescos já limpos e escamados dispostos na tábua de corte de madeira.',
            'o_que_ajustar': 'Realçar a textura fresca das escamas, os cortes culinários e o aspecto apetitoso do peixe de água doce pronto para o preparo. Iluminação focada na tábua.',
            'prompt_en': 'Rustic culinary still life photography of freshly caught river fish, cleaned and seasoned on a wooden cutting board ready for frying, sharp textures of fish scales and fresh cuts, natural kitchen light, authentic Brazilian river cooking tradition, close up shot, 50mm f/2.8, no CGI smoothing.',
            'prompt_pt': 'Foto culinária rústica de peixes frescos de rio limpos e retalhados sobre tábua de madeira prontos para assar ou fritar. Realce de nitidez nas escamas e na textura da carne fresca, iluminação gastronômica acolhedora.'
        }
    },
    '06-como-chegar': {
        'estrada-acesso-fachada-rancho.jpg': {
            'tipo': 'Inpainting / Remoção de Carimbo / Enquadramento de Chegada',
            'o_que_manter': 'A estrada de terra sombreada que dá acesso à casa do rancho, o céu azul límpido e a cerca com coqueiro.',
            'o_que_ajustar': 'REMOVER OBRIGATORIAMENTE o carimbo de data ("22 de março de 2026 13:20"). Realçar as cores naturais da terra e da vegetação para acolher o visitante.',
            'prompt_en': 'Scenic dirt road approach leading to a welcoming countryside retreat home, bright blue sky with white clouds, green trees lining the sunny path, small palm tree, remove date stamp watermark, authentic rural road photograph, sharp natural textures, documentary travel style, no 3D rendering.',
            'prompt_pt': 'Foto da estrada de terra de chegada ao rancho com céu azul ensolarado e árvores na beira do caminho. Remover o carimbo de data. Cores naturais e acolhedoras para guiar o hóspede na seção Como Chegar, sem render 3D.'
        },
        'casa-rancho-gramado-arvores.jpg': {
            'tipo': 'Inpainting / Remoção de Carimbo / Correção de Contraluz',
            'o_que_manter': 'A fachada da casa azul, as árvores nativas altas e a área verde do rancho.',
            'o_que_ajustar': 'REMOVER o carimbo de data. Suavizar o poste em primeiro plano ou dar foco à casa azul em meio à natureza.',
            'prompt_en': 'Clear outdoor photograph of a blue painted country lodge building set among tall native trees and green lawn, bright midday sun and blue sky, remove date watermark, clean exposure, realistic architectural nature photography, no artificial CGI.',
            'prompt_pt': 'Visão da casa azul do rancho entre árvores altas e gramado. Remover o carimbo de data. Iluminação natural e límpida, mantendo as características reais da propriedade.'
        }
    }
}

total_files_created = 0

for base_path in paths:
    if not os.path.exists(base_path):
        os.makedirs(base_path, exist_ok=True)
        
    for cat, imgs in prompts_data.items():
        cat_dir = os.path.join(base_path, cat)
        os.makedirs(cat_dir, exist_ok=True)
        
        # 1. Arquivo de resumo geral da pasta: PROMPTS_E_DIRETRIZES.md
        summary_md_path = os.path.join(cat_dir, 'PROMPTS_E_DIRETRIZES.md')
        summary_content = f'# Diretrizes de Tratamento Visual - {cat}\n\n'
        summary_content += '> **REGRA CRUCIAL:** Preservar a estrutura original, materiais reais (madeira, areia, água, alumínio) e rusticidade do rancho. **NUNCA DEIXAR COM CARA DE RENDER LISO DE IA OU 3D.**\n\n---\n\n'
        
        for img_name, data in imgs.items():
            summary_content += f'## 📸 {img_name}\n'
            summary_content += f'- **Tipo de Ajuste:** {data["tipo"]}\n'
            summary_content += f'- **O Que Manter:** {data["o_que_manter"]}\n'
            summary_content += f'- **O Que Ajustar / Limpar:** {data["o_que_ajustar"]}\n\n'
            summary_content += '### Prompt em Inglês (Para IA / Magnific / Midjourney / FLUX):\n'
            summary_content += '```text\n' + data['prompt_en'] + '\n```\n\n'
            summary_content += '### Instrução em Português (Para Photoshop / Designer):\n'
            summary_content += f'> {data["prompt_pt"]}\n\n---\n\n'
            
            # 2. Arquivo individual dedicado para cada imagem: <nome-da-imagem>.prompt.txt
            base_img_name = os.path.splitext(img_name)[0]
            indiv_prompt_path = os.path.join(cat_dir, f'{base_img_name}.prompt.txt')
            
            indiv_content = f'=================================================================\n'
            indiv_content += f'PROMPT DE TRATAMENTO / AJUSTE: {img_name}\n'
            indiv_content += f'=================================================================\n\n'
            indiv_content += f'DIRETIVA: {data["tipo"]}\n\n'
            indiv_content += f'[1] O QUE DEVE SER PRESERVADO (NÃO ALTERAR):\n{data["o_que_manter"]}\n\n'
            indiv_content += f'[2] O QUE DEVE SER AJUSTADO / CORRIGIDO:\n{data["o_que_ajustar"]}\n\n'
            indiv_content += f'[3] PROMPT PRONTO PARA IA (Magnific / Midjourney / FLUX / Inpainting):\n'
            indiv_content += f'{data["prompt_en"]}\n\n'
            indiv_content += f'[4] DIRETRIZ EM PORTUGUÊS (Photoshop / Lightroom / Generative Fill):\n'
            indiv_content += f'{data["prompt_pt"]}\n\n'
            indiv_content += f'AVISO: Manter a granulação e imperfeições naturais da foto real. Não aplicar filtros que deixem texturas plásticas ou com cara de maquete 3D.\n'
            
            with open(indiv_prompt_path, 'w', encoding='utf-8') as pf:
                pf.write(indiv_content)
            total_files_created += 1
            
        with open(summary_md_path, 'w', encoding='utf-8') as sf:
            sf.write(summary_content)
        total_files_created += 1

print(f'Total de arquivos de prompts criados com sucesso: {total_files_created}')
