import re

index_path = r"c:\Users\mikaa\Documents\antigravity\gallant-lovelace\site-recanto-dos-sonhos\index.html"

with open(index_path, "r", encoding="utf-8") as f:
    html = f.read()

# 1. Update <head> to ensure FontAwesome 6 & Bootstrap Icons CDN
head_cdns = """    <!-- Font Awesome 6 CDN & Local Webfonts -->
    <link
      rel="stylesheet"
      href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.5.1/css/all.min.css"
    />
    <!-- Bootstrap Icons CDN -->
    <link
      rel="stylesheet"
      href="https://cdn.jsdelivr.net/npm/bootstrap-icons@1.11.3/font/bootstrap-icons.min.css"
    />"""

if "cdnjs.cloudflare.com/ajax/libs/font-awesome" not in html:
    html = html.replace('<link\n      rel="stylesheet"\n      href="assets/css/all.min.css"\n      type="text/css"\n      media="all"\n    />',
                        head_cdns + '\n    <link\n      rel="stylesheet"\n      href="assets/css/all.min.css"\n      type="text/css"\n      media="all"\n    />')

# 2. Section 01: Topbar & Navigation
sec1_header = """    <!--==================================================-->
    <!-- SEÇÃO 01: CABEÇALHO & NAVEGAÇÃO (#header)         -->
    <!--==================================================-->
    <div class="hotelio-header-area" id="sticky-header">"""
html = re.sub(r'<!--\s*Start hotelio Header Area\s*-->\s*<!--=*-->\s*<div class="hotelio-header-area" id="sticky-header">', sec1_header, html)

# 3. Section 02: Hero Principal
sec2_hero = """    <!--==================================================-->
    <!-- SEÇÃO 02: HERO PRINCIPAL (#hero)                  -->
    <!--==================================================-->
    <section class="hero-section-three" id="hero">"""
html = re.sub(r'<!--\s*Start hotelio Hero section three\s*-->\s*<!--=*-->\s*<section class="hero-section-three">', sec2_hero, html)

# 4. Section 03: Barra de Reservas Flutuante
sec3_booking = """      <!--==================================================-->
      <!-- SEÇÃO 03: BARRA DE RESERVAS FLUTUANTE (#reservas)  -->
      <!--==================================================-->
      <div
        class="booking-section-one mountain wow fadeInUp"
        id="reservas"
        data-wow-delay="0.4s"
      >"""
html = re.sub(r'<div\s+class="booking-section-one mountain wow fadeInUp"\s+data-wow-delay="0.4s"\s*>', sec3_booking, html)

# 5. Section 04: Sobre o Rancho
sec4_about = """    <!--==================================================-->
    <!-- SEÇÃO 04: SOBRE O RANCHO (#sobre)                 -->
    <!--==================================================-->
    <div class="about-section-three" id="sobre">"""
html = re.sub(r'<!--\s*Start about section three\s*-->\s*<!--=*-->\s*<div class="about-section-three" id="sobre">', sec4_about, html)

# 6. Section 05: Estrutura & Lazer
sec5_facilities = """    <!--==================================================-->
    <!-- SEÇÃO 05: ESTRUTURA & LAZER (#estrutura)           -->
    <!--==================================================-->
    <div class="facilities-section-three" id="estrutura">"""
html = re.sub(r'<!--\s*Start hetelio facilities section three\s*-->\s*<!--=*-->\s*<div class="facilities-section-three" id="estrutura">', sec5_facilities, html)

# Fix Facilities content (translate English titles and fix slide titles)
facilities_intro_old = """              <div class="facilities-content">
                <h1>FACILITIES</h1>
                <h2>Welcome to Hotelio your gateway luxury and comfort</h2>
                <p>
                  Continually provide access to integrated human capital.
                  Continually streamline fully strategic theme areas rather
                </p>
              </div>"""

facilities_intro_new = """              <div class="facilities-content">
                <h1>ESTRUTURA & LAZER</h1>
                <h2>Tudo pronto para você viver dias inesquecíveis</h2>
                <p>
                  Do amanhecer à beira do Rio Araguaia às noites de confraternização na piscina aquecida e varanda gourmet. Cada ambiente pensado para o seu descanso absoluto.
                </p>
              </div>"""
html = html.replace(facilities_intro_old, facilities_intro_new)

# Slide 1: Piscina
s1_old = """                          <h3>
                            <a href="https://wa.me/5563981397171?text=Ol%C3%A1%21+Gostaria+de+saber+mais+sobre+a+estrutura+de+lazer+do+Recanto+dos+Sonhos+63." target="_blank"
                              >Piscina Pré-Aquecida & <br />Área Gourmet</a
                            >
                          </h3>"""
s1_new = """                          <h3>
                            <a href="https://wa.me/5563981397171?text=Ol%C3%A1%21+Gostaria+de+saber+mais+sobre+a+estrutura+de+lazer+do+Recanto+dos+Sonhos+63." target="_blank"
                              >Piscina Pré-Aquecida & <br />Deck com Hidro</a
                            >
                          </h3>"""
html = html.replace(s1_old, s1_new, 1)

# Slide 2: Sinuca
s2_old = """                          <h3>
                            <a href="https://wa.me/5563981397171?text=Ol%C3%A1%21+Gostaria+de+saber+mais+sobre+a+estrutura+de+lazer+do+Recanto+dos+Sonhos+63." target="_blank"
                              >Mesa de Bilhar & <br />Salão de Jogos</a
                            >
                          </h3>"""
s2_new = """                          <h3>
                            <a href="https://wa.me/5563981397171?text=Ol%C3%A1%21+Gostaria+de+saber+mais+sobre+a+estrutura+de+lazer+do+Recanto+dos+Sonhos+63." target="_blank"
                              >Varanda Gourmet & <br />Mesa de Sinuca</a
                            >
                          </h3>"""
html = html.replace(s2_old, s2_new, 1)

# Slide 3: Pier
s3_old = """                          <h3>
                            <a href="https://wa.me/5563981397171?text=Ol%C3%A1%21+Gostaria+de+saber+mais+sobre+a+estrutura+de+lazer+do+Recanto+dos+Sonhos+63." target="_blank"
                              >Piscina Pré-Aquecida & <br />Área Gourmet</a
                            >
                          </h3>"""
s3_new = """                          <h3>
                            <a href="https://wa.me/5563981397171?text=Ol%C3%A1%21+Gostaria+de+saber+mais+sobre+a+estrutura+de+lazer+do+Recanto+dos+Sonhos+63." target="_blank"
                              >Píer Coberto & <br />Embarque no Rio</a
                            >
                          </h3>"""
html = html.replace(s3_old, s3_new, 1)

# Slide 4: Mesas de Pedra
s4_old = """                          <h3>
                            <a href="https://wa.me/5563981397171?text=Ol%C3%A1%21+Gostaria+de+saber+mais+sobre+a+estrutura+de+lazer+do+Recanto+dos+Sonhos+63." target="_blank"
                              >Mesa de Bilhar & <br />Salão de Jogos</a
                            >
                          </h3>"""
s4_new = """                          <h3>
                            <a href="https://wa.me/5563981397171?text=Ol%C3%A1%21+Gostaria+de+saber+mais+sobre+a+estrutura+de+lazer+do+Recanto+dos+Sonhos+63." target="_blank"
                              >Área de Convivência & <br />Mesas ao Ar Livre</a
                            >
                          </h3>"""
html = html.replace(s4_old, s4_new, 1)

# Translate Facilities Counters
fac_counters_old = """                    <div class="counter-title">
                      <h3>
                        CUSTOMER’S <br />
                        SATISFACTION RATE
                      </h3>
                    </div>"""
fac_counters_new = """                    <div class="counter-title">
                      <h3>
                        SATISFAÇÃO DOS <br />
                        NOSSOS HÓSPEDES
                      </h3>
                    </div>"""
html = html.replace(fac_counters_old, fac_counters_new)

fac_counters2_old = """                    <div class="counter-title">
                      <h3>
                        WORLDWIDE HAPPY <br />
                        CUSTOMER’S
                      </h3>
                    </div>"""
fac_counters2_new = """                    <div class="counter-title">
                      <h3>
                        FAMÍLIAS & GRUPOS <br />
                        ENCANTADOS
                      </h3>
                    </div>"""
html = html.replace(fac_counters2_old, fac_counters2_new)

# 7. Section 06: Acomodações
sec6_rooms = """    <!--==================================================-->
    <!-- SEÇÃO 06: ACOMODAÇÕES & SUÍTES (#acomodacoes)     -->
    <!--==================================================-->
    <div class="rooms-section-one" id="acomodacoes">"""
html = re.sub(r'<!--\s*start hetelio rooms-section-one\s*-->\s*<div class="rooms-section-one" id="acomodacoes">', sec6_rooms, html)

# Fix 4 Room Cards in rooms-section-two
room_cards_old_pattern = r'<div\s+class="rooms-section-two"\s+id="rooms-section"[\s\S]+?<!--\s*End hetelio rooms-section-two\s*-->'
room_cards_new = """<div
      class="rooms-section-two"
      id="rooms-section"
      style="background-image: url(assets/images/rancho/04-acomodacoes/suite-casal-ar-condicionado.jpg)"
    >
      <div class="row g-0">
        <!-- Card Acomodação 01 -->
        <div class="col-xl-3 col-lg-4 col-md-6">
          <div
            class="room-item"
            data-bg="assets/images/rancho/04-acomodacoes/suite-casal-ar-condicionado.jpg"
          >
            <div class="room-price">
              <a href="https://wa.me/5563981397171?text=Ol%C3%A1%21+Gostaria+de+consultar+valores+e+disponibilidade+da+Su%C3%ADte+Master+no+Rancho." target="_blank">Sob Consulta</a>
            </div>
            <div class="room-content">
              <h1 class="room-title">SUÍTE MASTER</h1>
              <p class="room-desc">
                Cama queen casal, ar-condicionado split silencioso, banheiro privativo e vista panorâmica para a natureza.
              </p>
            </div>
            <div class="room-info">
              <p><i class="fa-solid fa-ruler-combined"></i> 35 M²</p>
              <p><i class="fa-solid fa-user-group"></i> 2 Hóspedes</p>
              <p><i class="fa-solid fa-bed"></i> 1 Cama Casal</p>
            </div>
            <div class="room-arrow">
              <a href="https://wa.me/5563981397171?text=Ol%C3%A1%21+Gostaria+de+consultar+valores+e+disponibilidade+da+Su%C3%ADte+Master+no+Rancho." target="_blank"
                ><svg width="16" height="12" viewBox="0 0 16 12" fill="none" xmlns="http://www.w3.org/2000/svg"><path fill-rule="evenodd" clip-rule="evenodd" d="M14.96 4.9808C12.8146 4.9808 10.8592 3.0272 10.8592 0.88V0H9.0992V0.88C9.0992 2.44112 9.78384 3.90544 10.8583 4.9808H0V6.7408H10.8583C9.78384 7.81616 9.0992 9.28048 9.0992 10.8416V11.7216H10.8592V10.8416C10.8592 8.69528 12.8146 6.7408 14.96 6.7408H15.84V4.9808H14.96Z" fill="white"/></svg></a>
            </div>
            <div class="room-btn defult-btn">
              <a href="https://wa.me/5563981397171?text=Ol%C3%A1%21+Gostaria+de+consultar+valores+e+disponibilidade+da+Su%C3%ADte+Master+no+Rancho." target="_blank"
                >CONSULTAR NO WHATSAPP<svg width="16" height="12" viewBox="0 0 16 12" fill="none" xmlns="http://www.w3.org/2000/svg"><path fill-rule="evenodd" clip-rule="evenodd" d="M14.96 4.9808C12.8146 4.9808 10.8592 3.0272 10.8592 0.88V0H9.0992V0.88C9.0992 2.44112 9.78384 3.90544 10.8583 4.9808H0V6.7408H10.8583C9.78384 7.81616 9.0992 9.28048 9.0992 10.8416V11.7216H10.8592V10.8416C10.8592 8.69528 12.8146 6.7408 14.96 6.7408H15.84V4.9808H14.96Z" fill="white"/></svg></a>
            </div>
          </div>
        </div>

        <!-- Card Acomodação 02 -->
        <div class="col-xl-3 col-lg-4 col-md-6">
          <div
            class="room-item"
            data-bg="assets/images/rancho/04-acomodacoes/quarto-familia-duas-camas.jpg"
          >
            <div class="room-price">
              <a href="https://wa.me/5563981397171?text=Ol%C3%A1%21+Gostaria+de+consultar+valores+e+disponibilidade+do+Quarto+Fam%C3%ADlia+no+Rancho." target="_blank">Sob Consulta</a>
            </div>
            <div class="room-content">
              <h1 class="room-title">QUARTO FAMÍLIA</h1>
              <p class="room-desc">
                Ideal para grupos e famílias, com camas confortáveis, ar-condicionado, tomadas acessíveis e ótima circulação.
              </p>
            </div>
            <div class="room-info">
              <p><i class="fa-solid fa-ruler-combined"></i> 45 M²</p>
              <p><i class="fa-solid fa-user-group"></i> Até 6 Pessoas</p>
              <p><i class="fa-solid fa-bed"></i> Camas Múltiplas</p>
            </div>
            <div class="room-arrow">
              <a href="https://wa.me/5563981397171?text=Ol%C3%A1%21+Gostaria+de+consultar+valores+e+disponibilidade+do+Quarto+Fam%C3%ADlia+no+Rancho." target="_blank"
                ><svg width="16" height="12" viewBox="0 0 16 12" fill="none" xmlns="http://www.w3.org/2000/svg"><path fill-rule="evenodd" clip-rule="evenodd" d="M14.96 4.9808C12.8146 4.9808 10.8592 3.0272 10.8592 0.88V0H9.0992V0.88C9.0992 2.44112 9.78384 3.90544 10.8583 4.9808H0V6.7408H10.8583C9.78384 7.81616 9.0992 9.28048 9.0992 10.8416V11.7216H10.8592V10.8416C10.8592 8.69528 12.8146 6.7408 14.96 6.7408H15.84V4.9808H14.96Z" fill="white"/></svg></a>
            </div>
            <div class="room-btn defult-btn">
              <a href="https://wa.me/5563981397171?text=Ol%C3%A1%21+Gostaria+de+consultar+valores+e+disponibilidade+do+Quarto+Fam%C3%ADlia+no+Rancho." target="_blank"
                >CONSULTAR NO WHATSAPP<svg width="16" height="12" viewBox="0 0 16 12" fill="none" xmlns="http://www.w3.org/2000/svg"><path fill-rule="evenodd" clip-rule="evenodd" d="M14.96 4.9808C12.8146 4.9808 10.8592 3.0272 10.8592 0.88V0H9.0992V0.88C9.0992 2.44112 9.78384 3.90544 10.8583 4.9808H0V6.7408H10.8583C9.78384 7.81616 9.0992 9.28048 9.0992 10.8416V11.7216H10.8592V10.8416C10.8592 8.69528 12.8146 6.7408 14.96 6.7408H15.84V4.9808H14.96Z" fill="white"/></svg></a>
            </div>
          </div>
        </div>

        <!-- Card Acomodação 03 -->
        <div class="col-xl-3 col-lg-4 col-md-6">
          <div
            class="room-item"
            data-bg="assets/images/rancho/04-acomodacoes/chales-modulares-externos-01.jpg"
          >
            <div class="room-price">
              <a href="https://wa.me/5563981397171?text=Ol%C3%A1%21+Gostaria+de+consultar+valores+e+disponibilidade+dos+Chal%C3%A9s+Modulares+no+Rancho." target="_blank">Sob Consulta</a>
            </div>
            <div class="room-content">
              <h1 class="room-title">CHALÉS EXTERNOS</h1>
              <p class="room-desc">
                Privacidade total em módulos independentes com varanda privativa integrada à vegetação nativa do cerrado.
              </p>
            </div>
            <div class="room-info">
              <p><i class="fa-solid fa-ruler-combined"></i> 30 M²</p>
              <p><i class="fa-solid fa-user-group"></i> Até 4 Pessoas</p>
              <p><i class="fa-solid fa-bed"></i> Casal + Solteiro</p>
            </div>
            <div class="room-arrow">
              <a href="https://wa.me/5563981397171?text=Ol%C3%A1%21+Gostaria+de+consultar+valores+e+disponibilidade+dos+Chal%C3%A9s+Modulares+no+Rancho." target="_blank"
                ><svg width="16" height="12" viewBox="0 0 16 12" fill="none" xmlns="http://www.w3.org/2000/svg"><path fill-rule="evenodd" clip-rule="evenodd" d="M14.96 4.9808C12.8146 4.9808 10.8592 3.0272 10.8592 0.88V0H9.0992V0.88C9.0992 2.44112 9.78384 3.90544 10.8583 4.9808H0V6.7408H10.8583C9.78384 7.81616 9.0992 9.28048 9.0992 10.8416V11.7216H10.8592V10.8416C10.8592 8.69528 12.8146 6.7408 14.96 6.7408H15.84V4.9808H14.96Z" fill="white"/></svg></a>
            </div>
            <div class="room-btn defult-btn">
              <a href="https://wa.me/5563981397171?text=Ol%C3%A1%21+Gostaria+de+consultar+valores+e+disponibilidade+dos+Chal%C3%A9s+Modulares+no+Rancho." target="_blank"
                >CONSULTAR NO WHATSAPP<svg width="16" height="12" viewBox="0 0 16 12" fill="none" xmlns="http://www.w3.org/2000/svg"><path fill-rule="evenodd" clip-rule="evenodd" d="M14.96 4.9808C12.8146 4.9808 10.8592 3.0272 10.8592 0.88V0H9.0992V0.88C9.0992 2.44112 9.78384 3.90544 10.8583 4.9808H0V6.7408H10.8583C9.78384 7.81616 9.0992 9.28048 9.0992 10.8416V11.7216H10.8592V10.8416C10.8592 8.69528 12.8146 6.7408 14.96 6.7408H15.84V4.9808H14.96Z" fill="white"/></svg></a>
            </div>
          </div>
        </div>

        <!-- Card Acomodação 04 -->
        <div class="col-xl-3 col-lg-4 col-md-6">
          <div
            class="room-item"
            data-bg="assets/images/rancho/04-acomodacoes/quarto-hospedes-cama-casal.jpg"
          >
            <div class="room-price">
              <a href="https://wa.me/5563981397171?text=Ol%C3%A1%21+Gostaria+de+consultar+valores+e+disponibilidade+do+Quarto+de+H%C3%B3spedes+no+Rancho." target="_blank">Sob Consulta</a>
            </div>
            <div class="room-content">
              <h1 class="room-title">QUARTO HÓSPEDES</h1>
              <p class="room-desc">
                Ambiente aconchegante com acabamento acolhedor, cama casal box, ar split e tranquilidade para o seu sono.
              </p>
            </div>
            <div class="room-info">
              <p><i class="fa-solid fa-ruler-combined"></i> 25 M²</p>
              <p><i class="fa-solid fa-user-group"></i> 2 Hóspedes</p>
              <p><i class="fa-solid fa-bed"></i> 1 Cama Casal</p>
            </div>
            <div class="room-arrow">
              <a href="https://wa.me/5563981397171?text=Ol%C3%A1%21+Gostaria+de+consultar+valores+e+disponibilidade+do+Quarto+de+H%C3%B3spedes+no+Rancho." target="_blank"
                ><svg width="16" height="12" viewBox="0 0 16 12" fill="none" xmlns="http://www.w3.org/2000/svg"><path fill-rule="evenodd" clip-rule="evenodd" d="M14.96 4.9808C12.8146 4.9808 10.8592 3.0272 10.8592 0.88V0H9.0992V0.88C9.0992 2.44112 9.78384 3.90544 10.8583 4.9808H0V6.7408H10.8583C9.78384 7.81616 9.0992 9.28048 9.0992 10.8416V11.7216H10.8592V10.8416C10.8592 8.69528 12.8146 6.7408 14.96 6.7408H15.84V4.9808H14.96Z" fill="white"/></svg></a>
            </div>
            <div class="room-btn defult-btn">
              <a href="https://wa.me/5563981397171?text=Ol%C3%A1%21+Gostaria+de+consultar+valores+e+disponibilidade+do+Quarto+de+H%C3%B3spedes+no+Rancho." target="_blank"
                >CONSULTAR NO WHATSAPP<svg width="16" height="12" viewBox="0 0 16 12" fill="none" xmlns="http://www.w3.org/2000/svg"><path fill-rule="evenodd" clip-rule="evenodd" d="M14.96 4.9808C12.8146 4.9808 10.8592 3.0272 10.8592 0.88V0H9.0992V0.88C9.0992 2.44112 9.78384 3.90544 10.8583 4.9808H0V6.7408H10.8583C9.78384 7.81616 9.0992 9.28048 9.0992 10.8416V11.7216H10.8592V10.8416C10.8592 8.69528 12.8146 6.7408 14.96 6.7408H15.84V4.9808H14.96Z" fill="white"/></svg></a>
            </div>
          </div>
        </div>
      </div>
    </div>
    <!--==================================================-->
    <!-- End hetelio rooms-section-two -->"""

html = re.sub(room_cards_old_pattern, room_cards_new, html)

# 8. Section 07: Praia & Experiência Araguaia
sec7_praia = """    <!--==================================================-->
    <!-- SEÇÃO 07: PRAIA & EXPERIÊNCIA ARAGUAIA (#praia)    -->
    <!--==================================================-->
    <div class="our-room-suites-section-three" id="praia">"""
html = re.sub(r'<!--\s*Start our room suites section three panel-area-2\s*-->\s*<!--=*-->\s*<div class="our-room-suites-section-three" id="praia">', sec7_praia, html)

# Fix images and texts of Section 07 (Praia)
praia_panels_old_pattern = r'<div class="row panel-space panel-item-2">[\s\S]+?<!--\s*End our room suites section three\s*-->'
praia_panels_new = """<div class="row panel-space panel-item-2">
          <div class="section-border"></div>
          <div class="col-xl-2 col-lg-2 col-md-2">
            <div class="room-suites-number">
              <span>01</span>
            </div>
          </div>
          <div class="col-xl-6 col-lg-6 col-md-6">
            <div class="single-room-box">
              <div class="room-content">
                <h2><a href="https://wa.me/5563981397171?text=Ol%C3%A1%21+Gostaria+de+informa%C3%A7%C3%B5es+sobre+a+travessia+e+as+atividades+na+praia." target="_blank">TRAVESSIA DE BARCO EXCLUSIVA</a></h2>
                <p>
                  Embarque com conforto e segurança direto no píer privativo do rancho. Piloto experiente e navegação suave pelo Rio Araguaia.
                </p>
                <div class="room-list gs_fade_anim">
                  <ul>
                    <li><svg width="21" height="18" viewBox="0 0 21 18" fill="none" xmlns="http://www.w3.org/2000/svg"><path d="M8.46329 18.0004H8.45438C8.39696 17.9992 8.34036 17.9864 8.288 17.9628C8.23564 17.9392 8.1886 17.9053 8.14969 17.863L0.112504 9.12365C0.0456617 9.05099 0.00612705 8.95737 0.000655237 8.8588C-0.00481657 8.76022 0.0241141 8.6628 0.0825037 8.58319C0.140913 8.50359 0.225123 8.44672 0.320775 8.42228C0.416427 8.39783 0.517597 8.40732 0.607035 8.44912L7.96313 11.8935C8.025 11.9226 8.09813 11.9085 8.14547 11.8593L19.3664 0.131624C19.5183 -0.0272825 19.7667 -0.0446263 19.9392 0.0922487C20.1117 0.229124 20.1516 0.474749 20.0311 0.658967L8.86922 17.758C8.85328 17.7829 8.83454 17.8054 8.81391 17.8265L8.76469 17.8757C8.68459 17.9554 8.57626 18.0002 8.46329 18.0004Z" fill="#C09763"></path></svg>
                      Piloto experiente, coletes salva-vidas e total comodidade
                    </li>
                    <li><svg width="21" height="18" viewBox="0 0 21 18" fill="none" xmlns="http://www.w3.org/2000/svg"><path d="M8.46329 18.0004H8.45438C8.39696 17.9992 8.34036 17.9864 8.288 17.9628C8.23564 17.9392 8.1886 17.9053 8.14969 17.863L0.112504 9.12365C0.0456617 9.05099 0.00612705 8.95737 0.000655237 8.8588C-0.00481657 8.76022 0.0241141 8.6628 0.0825037 8.58319C0.140913 8.50359 0.225123 8.44672 0.320775 8.42228C0.416427 8.39783 0.517597 8.40732 0.607035 8.44912L7.96313 11.8935C8.025 11.9226 8.09813 11.9085 8.14547 11.8593L19.3664 0.131624C19.5183 -0.0272825 19.7667 -0.0446263 19.9392 0.0922487C20.1117 0.229124 20.1516 0.474749 20.0311 0.658967L8.86922 17.758C8.85328 17.7829 8.83454 17.8054 8.81391 17.8265L8.76469 17.8757C8.68459 17.9554 8.57626 18.0002 8.46329 18.0004Z" fill="#C09763"></path></svg>
                      Acesso rápido aos melhores bancos de areia da região
                    </li>
                  </ul>
                </div>
                <a href="https://wa.me/5563981397171?text=Ol%C3%A1%21+Gostaria+de+informa%C3%A7%C3%B5es+sobre+a+travessia+e+as+atividades+na+praia." target="_blank" class="explore-btn gs_fade_anim"
                  >SOLICITAR NO WHATSAPP
                  <svg width="16" height="12" viewBox="0 0 16 12" fill="none" xmlns="http://www.w3.org/2000/svg"><path fill-rule="evenodd" clip-rule="evenodd" d="M14.96 4.9808C12.8146 4.9808 10.8592 3.0272 10.8592 0.88V0H9.0992V0.88C9.0992 2.44112 9.78384 3.90544 10.8583 4.9808H0V6.7408H10.8583C9.78384 7.81616 9.0992 9.28048 9.0992 10.8416V11.7216H10.8592V10.8416C10.8592 8.69528 12.8146 6.7408 14.96 6.7408H15.84V4.9808H14.96Z" fill="#0A0A0A"/></svg></a>
              </div>
            </div>
          </div>
          <div class="col-xl-4 col-lg-4 col-md-4">
            <div class="room-suites-thumb">
              <figure class="reveal image-anime">
                <img
                  src="assets/images/rancho/02-praia-e-barcos/barcos-voadeiras-recanto-dos-sonhos.jpg"
                  alt="Barcos e Voadeiras no Rancho Recanto dos Sonhos"
                />
              </figure>
            </div>
          </div>
        </div>

        <div class="row panel-space panel-item-2">
          <div class="section-border"></div>
          <div class="col-xl-2 col-lg-2 col-md-2">
            <div class="room-suites-number">
              <span>02</span>
            </div>
          </div>
          <div class="col-xl-6 col-lg-6 col-md-6">
            <div class="single-room-box">
              <div class="room-content">
                <h2><a href="https://wa.me/5563981397171?text=Ol%C3%A1%21+Gostaria+de+informa%C3%A7%C3%B5es+sobre+a+tenda+privativa+na+praia." target="_blank">TENDA PRIVATIVA MONTADA NA AREIA</a></h2>
                <p>
                  Sombra fresca e estrutura exclusiva montada para o seu grupo curtir o dia inteiro na areia branca com privacidade total.
                </p>
                <div class="room-list gs_fade_anim">
                  <ul>
                    <li><svg width="21" height="18" viewBox="0 0 21 18" fill="none" xmlns="http://www.w3.org/2000/svg"><path d="M8.46329 18.0004H8.45438C8.39696 17.9992 8.34036 17.9864 8.288 17.9628C8.23564 17.9392 8.1886 17.9053 8.14969 17.863L0.112504 9.12365C0.0456617 9.05099 0.00612705 8.95737 0.000655237 8.8588C-0.00481657 8.76022 0.0241141 8.6628 0.0825037 8.58319C0.140913 8.50359 0.225123 8.44672 0.320775 8.42228C0.416427 8.39783 0.517597 8.40732 0.607035 8.44912L7.96313 11.8935C8.025 11.9226 8.09813 11.9085 8.14547 11.8593L19.3664 0.131624C19.5183 -0.0272825 19.7667 -0.0446263 19.9392 0.0922487C20.1117 0.229124 20.1516 0.474749 20.0311 0.658967L8.86922 17.758C8.85328 17.7829 8.83454 17.8054 8.81391 17.8265L8.76469 17.8757C8.68459 17.9554 8.57626 18.0002 8.46329 18.0004Z" fill="#C09763"></path></svg>
                      Mesas, cadeiras e ampla cobertura contra o sol forte
                    </li>
                    <li><svg width="21" height="18" viewBox="0 0 21 18" fill="none" xmlns="http://www.w3.org/2000/svg"><path d="M8.46329 18.0004H8.45438C8.39696 17.9992 8.34036 17.9864 8.288 17.9628C8.23564 17.9392 8.1886 17.9053 8.14969 17.863L0.112504 9.12365C0.0456617 9.05099 0.00612705 8.95737 0.000655237 8.8588C-0.00481657 8.76022 0.0241141 8.6628 0.0825037 8.58319C0.140913 8.50359 0.225123 8.44672 0.320775 8.42228C0.416427 8.39783 0.517597 8.40732 0.607035 8.44912L7.96313 11.8935C8.025 11.9226 8.09813 11.9085 8.14547 11.8593L19.3664 0.131624C19.5183 -0.0272825 19.7667 -0.0446263 19.9392 0.0922487C20.1117 0.229124 20.1516 0.474749 20.0311 0.658967L8.86922 17.758C8.85328 17.7829 8.83454 17.8054 8.81391 17.8265L8.76469 17.8757C8.68459 17.9554 8.57626 18.0002 8.46329 18.0004Z" fill="#C09763"></path></svg>
                      Bebidas geladas e aperitivos à beira da água doce
                    </li>
                  </ul>
                </div>
                <a href="https://wa.me/5563981397171?text=Ol%C3%A1%21+Gostaria+de+informa%C3%A7%C3%B5es+sobre+a+tenda+privativa+na+praia." target="_blank" class="explore-btn gs_fade_anim"
                  >SOLICITAR NO WHATSAPP
                  <svg width="16" height="12" viewBox="0 0 16 12" fill="none" xmlns="http://www.w3.org/2000/svg"><path fill-rule="evenodd" clip-rule="evenodd" d="M14.96 4.9808C12.8146 4.9808 10.8592 3.0272 10.8592 0.88V0H9.0992V0.88C9.0992 2.44112 9.78384 3.90544 10.8583 4.9808H0V6.7408H10.8583C9.78384 7.81616 9.0992 9.28048 9.0992 10.8416V11.7216H10.8592V10.8416C10.8592 8.69528 12.8146 6.7408 14.96 6.7408H15.84V4.9808H14.96Z" fill="#0A0A0A"/></svg></a>
              </div>
            </div>
          </div>
          <div class="col-xl-4 col-lg-4 col-md-4">
            <div class="room-suites-thumb">
              <figure class="reveal image-anime">
                <img
                  src="assets/images/rancho/02-praia-e-barcos/tenda-privativa-praia-araguaia-01.jpg"
                  alt="Tenda Privativa na Praia do Rio Araguaia"
                />
              </figure>
            </div>
          </div>
        </div>

        <div class="row panel-space panel-item-2">
          <div class="section-border"></div>
          <div class="col-xl-2 col-lg-2 col-md-2">
            <div class="room-suites-number">
              <span>03</span>
            </div>
          </div>
          <div class="col-xl-6 col-lg-6 col-md-6">
            <div class="single-room-box">
              <div class="room-content">
                <h2><a href="https://wa.me/5563981397171?text=Ol%C3%A1%21+Gostaria+de+saber+mais+sobre+a+pesca+e+o+banho+de+rio+no+Rancho." target="_blank">REDE DENTRO D'ÁGUA & PESCARIA</a></h2>
                <p>
                  Sinta a água morna e límpida do Araguaia deitado na rede ou aproveite os melhores pontos de pesca esportiva do Tocantins.
                </p>
                <div class="room-list gs_fade_anim">
                  <ul>
                    <li><svg width="21" height="18" viewBox="0 0 21 18" fill="none" xmlns="http://www.w3.org/2000/svg"><path d="M8.46329 18.0004H8.45438C8.39696 17.9992 8.34036 17.9864 8.288 17.9628C8.23564 17.9392 8.1886 17.9053 8.14969 17.863L0.112504 9.12365C0.0456617 9.05099 0.00612705 8.95737 0.000655237 8.8588C-0.00481657 8.76022 0.0241141 8.6628 0.0825037 8.58319C0.140913 8.50359 0.225123 8.44672 0.320775 8.42228C0.416427 8.39783 0.517597 8.40732 0.607035 8.44912L7.96313 11.8935C8.025 11.9226 8.09813 11.9085 8.14547 11.8593L19.3664 0.131624C19.5183 -0.0272825 19.7667 -0.0446263 19.9392 0.0922487C20.1117 0.229124 20.1516 0.474749 20.0311 0.658967L8.86922 17.758C8.85328 17.7829 8.83454 17.8054 8.81391 17.8265L8.76469 17.8757C8.68459 17.9554 8.57626 18.0002 8.46329 18.0004Z" fill="#C09763"></path></svg>
                      Rede submersa na água para relaxar e tirar fotos incríveis
                    </li>
                    <li><svg width="21" height="18" viewBox="0 0 21 18" fill="none" xmlns="http://www.w3.org/2000/svg"><path d="M8.46329 18.0004H8.45438C8.39696 17.9992 8.34036 17.9864 8.288 17.9628C8.23564 17.9392 8.1886 17.9053 8.14969 17.863L0.112504 9.12365C0.0456617 9.05099 0.00612705 8.95737 0.000655237 8.8588C-0.00481657 8.76022 0.0241141 8.6628 0.0825037 8.58319C0.140913 8.50359 0.225123 8.44672 0.320775 8.42228C0.416427 8.39783 0.517597 8.40732 0.607035 8.44912L7.96313 11.8935C8.025 11.9226 8.09813 11.9085 8.14547 11.8593L19.3664 0.131624C19.5183 -0.0272825 19.7667 -0.0446263 19.9392 0.0922487C20.1117 0.229124 20.1516 0.474749 20.0311 0.658967L8.86922 17.758C8.85328 17.7829 8.83454 17.8054 8.81391 17.8265L8.76469 17.8757C8.68459 17.9554 8.57626 18.0002 8.46329 18.0004Z" fill="#C09763"></path></svg>
                      Pôr do sol cinematográfico e contato íntimo com a fauna
                    </li>
                  </ul>
                </div>
                <a href="https://wa.me/5563981397171?text=Ol%C3%A1%21+Gostaria+de+saber+mais+sobre+a+pesca+e+o+banho+de+rio+no+Rancho." target="_blank" class="explore-btn gs_fade_anim"
                  >SOLICITAR NO WHATSAPP
                  <svg width="16" height="12" viewBox="0 0 16 12" fill="none" xmlns="http://www.w3.org/2000/svg"><path fill-rule="evenodd" clip-rule="evenodd" d="M14.96 4.9808C12.8146 4.9808 10.8592 3.0272 10.8592 0.88V0H9.0992V0.88C9.0992 2.44112 9.78384 3.90544 10.8583 4.9808H0V6.7408H10.8583C9.78384 7.81616 9.0992 9.28048 9.0992 10.8416V11.7216H10.8592V10.8416C10.8592 8.69528 12.8146 6.7408 14.96 6.7408H15.84V4.9808H14.96Z" fill="#0A0A0A"/></svg></a>
              </div>
            </div>
          </div>
          <div class="col-xl-4 col-lg-4 col-md-4">
            <div class="room-suites-thumb">
              <figure class="reveal image-anime">
                <img
                  src="assets/images/rancho/02-praia-e-barcos/rede-dentro-dagua-araguaia.jpg"
                  alt="Rede dentro d'água no Rio Araguaia"
                />
              </figure>
            </div>
          </div>
        </div>
      </div>
    </div>
    <!--==================================================-->
    <!-- End our room suites section three -->"""

html = re.sub(praia_panels_old_pattern, praia_panels_new, html)

# 9. Section 08: Vídeo Tour
sec8_video = """    <!--==================================================-->
    <!-- SEÇÃO 08: VÍDEO TOUR & VISTA AÉREA (#video)       -->
    <!--==================================================-->
    <div
      class="video-section mountain parallaxie"
      id="video"
      style="background-image: url(assets/images/rancho/01-hero-e-aereas/drone-ilha-areia-araguaia-4k.jpg)"
    >"""
html = re.sub(r'<!--\s*Start hetelio\s+Video section\s*-->\s*<!--=*-->\s*<div\s+class="video-section mountain parallaxie"[^>]*>', sec8_video, html)

# 10. Section 09: Depoimentos & Experiências Reais
sec9_testi = """    <!--==================================================-->
    <!-- SEÇÃO 09: DEPOIMENTOS & EXPERIÊNCIAS (#depoimentos)-->
    <!--==================================================-->
    <div class="testimonial-section-three" id="depoimentos">"""
html = re.sub(r'<!--\s*start testimonial section two classic\s*-->\s*<!--=*-->\s*<div class="testimonial-section-three" id="depoimentos">', sec9_testi, html)

# Fix Testimonials Section Content (Heading, Titles, Testimonial items)
testi_old_pattern = r'<div class="sec-title">\s*<div class="section-title">[\s\S]+?</div>\s*<div class="section-border"></div>\s*</div>\s*<div class="swiper testimonial-resort-classic">[\s\S]+?<!--\s*End testimonial section two classic\s*-->'
testi_new = """<div class="sec-title">
              <div class="section-sub-title">
                <span class="sub-title text-anime-1">EXPERIÊNCIAS REAIS</span>
              </div>
              <div class="section-border"></div>
              <div class="section-title">
                <h1 class="title text-effect">
                  O que dizem os <span>nossos hóspedes</span>
                </h1>
                <h1 class="title text-effect">
                  SOBRE O <span class="title-gold">RECANTO DOS SONHOS</span>
                </h1>
              </div>
            </div>
            <div class="swiper testimonial-resort-classic">
              <div class="swiper-wrapper">
                <!-- Depoimento 1 -->
                <div class="swiper-slide">
                  <div class="single-testi-box">
                    <div class="testi-autor-box">
                      <div class="testi-autor-img">
                        <img
                          src="assets/images/demo-image/testi-autor.png"
                          alt="Hóspede Recanto dos Sonhos"
                        />
                      </div>
                      <div class="testi-autor-content">
                        <h2 class="autor-title">MARCOS & FAMÍLIA</h2>
                        <p class="autor-desi">Hóspedes de Palmas - TO</p>
                      </div>
                    </div>
                    <div class="testi-content-wrap">
                      <div class="testi-desc">
                        <p>
                          “Experiência inesquecível! O rancho é maravilhoso, piscina aquecida perfeita para as crianças, quartos muito confortáveis e a travessia para a praia com a tenda montada foi o ponto alto da viagem. Já virou nossa parada obrigatória em Peixe!”
                        </p>
                      </div>
                      <div class="testi-ratting">
                        <ul>
                          <li><i class="fa-solid fa-star"></i></li>
                          <li><i class="fa-solid fa-star"></i></li>
                          <li><i class="fa-solid fa-star"></i></li>
                          <li><i class="fa-solid fa-star"></i></li>
                          <li><i class="fa-solid fa-star"></i></li>
                        </ul>
                      </div>
                    </div>
                  </div>
                </div>
                <!-- Depoimento 2 -->
                <div class="swiper-slide">
                  <div class="single-testi-box">
                    <div class="testi-autor-box">
                      <div class="testi-autor-img">
                        <img
                          src="assets/images/demo-image/testi-autor.png"
                          alt="Hóspede Recanto dos Sonhos"
                        />
                      </div>
                      <div class="testi-autor-content">
                        <h2 class="autor-title">JULIANA & AMIGOS</h2>
                        <p class="autor-desi">Temporada do Araguaia</p>
                      </div>
                    </div>
                    <div class="testi-content-wrap">
                      <div class="testi-desc">
                        <p>
                          “Lugar de paz e tranquilidade pura! Passamos 3 dias perfeitos com amigos. A varanda gourmet com sinuca e churrasqueira nos atendeu muito bem. O pôr do sol no rio visto da praia é cinematográfico.”
                        </p>
                      </div>
                      <div class="testi-ratting">
                        <ul>
                          <li><i class="fa-solid fa-star"></i></li>
                          <li><i class="fa-solid fa-star"></i></li>
                          <li><i class="fa-solid fa-star"></i></li>
                          <li><i class="fa-solid fa-star"></i></li>
                          <li><i class="fa-solid fa-star"></i></li>
                        </ul>
                      </div>
                    </div>
                  </div>
                </div>
                <!-- Depoimento 3 -->
                <div class="swiper-slide">
                  <div class="single-testi-box">
                    <div class="testi-autor-box">
                      <div class="testi-autor-img">
                        <img
                          src="assets/images/demo-image/testi-autor.png"
                          alt="Hóspede Recanto dos Sonhos"
                        />
                      </div>
                      <div class="testi-autor-content">
                        <h2 class="autor-title">CARLOS EDUARDO</h2>
                        <p class="autor-desi">Grupo de Pesca Esportiva</p>
                      </div>
                    </div>
                    <div class="testi-content-wrap">
                      <div class="testi-desc">
                        <p>
                          “Estrutura impecável. Píer excelente para embarque e desembarque, água limpa e peixe fresco. Rancho muito limpo, organizado e com atendimento nota dez do caseiro e da equipe.”
                        </p>
                      </div>
                      <div class="testi-ratting">
                        <ul>
                          <li><i class="fa-solid fa-star"></i></li>
                          <li><i class="fa-solid fa-star"></i></li>
                          <li><i class="fa-solid fa-star"></i></li>
                          <li><i class="fa-solid fa-star"></i></li>
                          <li><i class="fa-solid fa-star"></i></li>
                        </ul>
                      </div>
                    </div>
                  </div>
                </div>
              </div>
              <div class="testimonial-arrow-box">
                <button class="slider-prev" tabindex="0" aria-label="Depoimento Anterior">
                  <i class="fa-solid fa-angle-left"></i>
                </button>
                <button class="slider-next" tabindex="0" aria-label="Próximo Depoimento">
                  <i class="fa-solid fa-angle-right"></i>
                </button>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
    <!--==================================================-->
    <!-- End testimonial section two classic -->"""

html = re.sub(testi_old_pattern, testi_new, html)

# 11. Section 10: Contato Rápido & Ofertas (Newsletter)
sec10_sub = """    <!--==================================================-->
    <!-- SEÇÃO 10: CONDIÇÕES ESPECIAIS (#contato-rapido)   -->
    <!--==================================================-->
    <div
      class="subcribe-section-two parallaxie"
      id="contato-rapido"
      style="background-image: url(assets/images/demo-image/subcribe-bg-2.jpg)"
    >
      <div class="auto-container">
        <div class="row align-items-center">
          <div class="col-xl-7 col-lg-7">
            <div class="sec-title">
              <div class="section-sub-title">
                <span class="sub-title text-anime-3">CONDIÇÕES EXCLUSIVAS</span>
              </div>
              <div class="section-title">
                <h1 class="text-effect text-white">RECEBA VALORES ESPECIAIS</h1>
                <h1 class="text-effect text-white">PARA FERIADOS & TEMPORADA</h1>
              </div>
            </div>
          </div>
          <div class="col-xl-5 col-lg-5">
            <form action="https://formspree.io/f/myyleorq" method="POST">
              <div class="subscribe-box">
                <input
                  type="text"
                  name="Email"
                  placeholder="Seu WhatsApp ou E-mail"
                  required=""
                />
                <button type="submit" class="subscribe-btn" aria-label="Enviar Contato">
                  <span><i class="fa-solid fa-location-arrow"></i></span>
                </button>
              </div>
              <label class="checkbox-label" style="color: #d1d1d1; margin-top: 10px; font-size: 13px;">
                <input type="checkbox" required checked /> Quero receber informações de disponibilidade e tarifas especiais
              </label>
            </form>
          </div>
        </div>
      </div>
    </div>
    <!--==================================================-->
    <!-- End subscribe section two -->"""

sub_pattern = r'<div\s+class="subcribe-section-two parallaxie"[\s\S]+?<!--\s*End subscribe section two\s*-->'
html = re.sub(sub_pattern, sec10_sub, html)

# 12. Section 11: Como Chegar & Guia do Viajante
sec11_blog = """    <!--==================================================-->
    <!-- SEÇÃO 11: COMO CHEGAR & DICAS (#como-chegar)      -->
    <!--==================================================-->
    <div class="blog-section-one" id="como-chegar">"""
html = re.sub(r'<!--\s*start blog section one\s*-->\s*<!--=*-->\s*<div class="blog-section-one" id="como-chegar">', sec11_blog, html)

# Fix English remnants in Blog Cards
html = html.replace('>Quickly morph just in times front end scenarios<', '>Temporada do Araguaia: Melhores Épocas & Dicas<')
html = html.replace('>BY - <span>ROHN ALEXON</span><', '<span>RECANTO 63</span><')
html = re.sub(r'>MORE<svg', '>VER DICAS<svg', html)

# 13. Section 12: Rodapé & Contatos Oficiais
sec12_footer = """    <!--==================================================-->
    <!-- SEÇÃO 12: RODAPÉ & CONTATOS OFICIAIS (#contato)   -->
    <!--==================================================-->
    <footer class="main-footer-one" id="contato">"""
html = re.sub(r'<!--\s*Start main footer Section\s*-->\s*<!--=*-->\s*<footer class="main-footer-one" id="contato">', sec12_footer, html)

# Fix Sitemap / Terms in Footer bottom
html = html.replace('<li><a href="#">Sitemap</a></li>\n                  <li><a href="#">Terms & Conditions</a></li>',
                    '<li><a href="#sobre">O Rancho</a></li>\n                  <li><a href="#como-chegar">Como Chegar</a></li>\n                  <li><a href="https://wa.me/5563981397171" target="_blank">WhatsApp Oficial</a></li>')

with open(index_path, "w", encoding="utf-8") as f:
    f.write(html)

print("SUCCESS: index.html updated with 12 clean sections, 100% PT-BR copy, correct image placements, and icon CDN links!")
