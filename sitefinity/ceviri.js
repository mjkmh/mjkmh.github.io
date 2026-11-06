/* MJKMH Sitefinity TR -> EN çevirici.
   window.__cevir(html) : Türkçe içerik bloğu HTML'ini İngilizceye çevirir.
   1) Tam metin eşleşmeleri (TAM), 2) parça değişimleri (PARCA), 3) iç bağlantı haritası (LINK). */
(function () {
  var TAM = {
    'Emekli Öğretim Üyelerimiz': 'Retired Faculty',
    'Emekli Öğretim Üyesi': 'Retired Faculty Member',
    /* --- Hakkımızda --- */
    "Mühendislik Jeolojisi-Kaya Mekaniği-Hidrojeoloji (MJKMH) Çalışma Grubunun Tarihçesi":
      "History of the Engineering Geology – Rock Mechanics – Hydrogeology (MJKMH) Working Group",
    "Mühendislik Jeolojisi-Kaya Mekaniği-Hidrojeoloji (MJKMH) Çalışma Grubunun kökleri, İstanbul Teknik Üniversitesinde yerbilimleri eğitiminin kurumsallaştığı yıllara uzanır. Ord. Prof. Dr. Ahmet Malik Sayar, 1944’ten itibaren İnşaat Fakültesinde jeoloji profesörü olarak görev yapmış, 1953’te kurulan Maden Fakültesinin kuruluşuna önemli katkılar sağlamış ve 1953–1955 yıllarında fakültenin dekanlığını yürütmüştür. Prof. Dr. Kemal Erguvanlı da fakültenin kuruluşunda görev alan bilim insanları arasındadır.":
      "The roots of the Engineering Geology – Rock Mechanics – Hydrogeology (MJKMH) Working Group go back to the years when earth science education was institutionalised at Istanbul Technical University. Ord. Prof. Dr. Ahmet Malik Sayar served as professor of geology at the Faculty of Civil Engineering from 1944, made major contributions to the founding of the Faculty of Mines in 1953 and served as its dean between 1953 and 1955. Prof. Dr. Kemal Erguvanlı was also among the scientists involved in the founding of the faculty.",
    "Grubun çalışma alanlarının temeli büyük ölçüde Prof. Dr. Kemal Erguvanlı’nın öncülüğünde atılmıştır. 1954–1957 yılları arasında Londra’daki Imperial College’da mühendislik jeolojisi üzerine araştırmalar yürüten Erguvanlı, Türkiye’de bu alanın gelişmesine öncülük etmiş; jeologların inşaat ve maden mühendisleri ile mimarlarla birlikte çalışmasını savunmuştur. Yol, köprü, baraj ve yeraltı suyu projelerine sunduğu katkılar, bugün grubun benimsediği disiplinler arası ve uygulamaya dönük yaklaşımın ilk örnekleridir. “Taş, toprak, su, işimiz bu!” sözü, bu anlayışın özeti olarak kuşaktan kuşağa aktarılmaktadır.":
      "The foundations of the group’s fields of study were largely laid under the leadership of Prof. Dr. Kemal Erguvanlı. Having carried out research on engineering geology at Imperial College London between 1954 and 1957, Erguvanlı pioneered the development of the field in Türkiye and advocated close collaboration between geologists, civil and mining engineers and architects. His contributions to road, bridge, dam and groundwater projects are early examples of the interdisciplinary, application-oriented approach the group follows today. His motto “Stone, soil, water – that is our job!” has been passed down from generation to generation as a summary of this approach.",
    "Bu birikim, sonraki kuşakta Prof. Dr. Erdoğan Yüzer ve Prof. Dr. Mahir Vardar ile genişlemiştir. Hidrojeoloji, mühendislik jeolojisi ve kaya mekaniği alanlarında çalışan, üç dönem Maden Fakültesi dekanlığı yapan Yüzer, Mühendislik Jeolojisi Türk Millî Komitesi Başkanlığı gibi görevlerle alanın ulusal düzeyde örgütlenmesine katkı sağlamıştır. Jeomekanik, tünelcilik ve kaya yapılarının tasarımı üzerine çalışan Vardar ise bölüm başkanlığı ve dekanlık görevlerinin yanında kırk yılı aşkın süre öğrenci yetiştirmiş, araştırmayı mühendislik uygulamalarıyla buluşturmuştur.":
      "This legacy was expanded by the next generation with Prof. Dr. Erdoğan Yüzer and Prof. Dr. Mahir Vardar. Yüzer, who worked in hydrogeology, engineering geology and rock mechanics and served three terms as dean of the Faculty of Mines, contributed to the national organisation of the discipline through roles such as chair of the Turkish National Committee of Engineering Geology. Vardar, who worked on geomechanics, tunnelling and the design of rock structures, trained students for more than forty years alongside his duties as head of department and dean, bringing research together with engineering practice.",
    "Bugün MJKMH Çalışma Grubu, hocalarımızdan devraldığı bu mirası mühendislik jeolojisi, kaya mekaniği ve hidrojeoloji alanlarındaki eğitim, araştırma ve uygulama çalışmalarıyla sürdürmektedir. Grubun adında bir araya gelen bu üç alan, Erguvanlı’nın ifadesiyle taşı, toprağı ve suyu birlikte ele alan bütüncül bir yerbilimleri anlayışının bugünkü karşılığıdır.":
      "Today the MJKMH Working Group carries this legacy forward through education, research and applied work in engineering geology, rock mechanics and hydrogeology. The three fields that come together in the group’s name are the present-day expression of a holistic view of the earth sciences that, in Erguvanlı’s words, treats stone, soil and water together.",
    "Hocalarımız": "Our Mentors",
    "(d. 1937)": "(b. 1937)",
    "1971 yılında İstanbul Teknik Üniversitesinden maden yüksek mühendisi unvanıyla mezun olan Mahir Vardar, 1977 yılına kadar Karlsruhe Teknik Üniversitesi İnşaat Fakültesinde araştırma görevlisi olarak çalışmış ve doktorasını tamamlamıştır. Ardından İTÜ Maden Fakültesinde doktor asistan olarak göreve başlamış, 1982 yılında doçentlik tezini sunmuş ve 1988 yılında profesör unvanını almıştır. Bölüm başkanlığı ve dekanlık görevlerini de üstlenen Vardar, 2017 yılında emekli olmuş, 3 Mayıs 2020 tarihinde aramızdan ayrılmıştır. Madencilik, mühendislik jeolojisi, jeomekanik, tünelcilik ve kaya yapılarının tasarımı alanlarında çalışan Vardar, çok sayıda mühendislik projesinin yürütülmesine ve Türkiye’de mühendislik hizmetlerinin gelişmesine katkı sağlamıştır. İTÜ’de kırk yılı aşkın süre boyunca öğrenciler yetiştirmiş, araştırma ve uygulama deneyimini eğitim anlayışıyla bütünleştirmiştir. Mühendislik sorunlarının bilimsel temelde ele alınmasına verdiği önem, hem mesleki çalışmalarına hem de öğrencileriyle kurduğu ilişkiye yansımıştır. Bilgisi, görgüsü ve ince zekâsıyla saygı duyulan hocamız, bilime inanan ve öğrencilerine değer veren çok yönlü kişiliğiyle hatırlanmaktadır. İnsan ve doğa sevgisiyle beslenen yaşam sevinci, mesleki birikimi ve yetiştirdiği öğrencilerle bıraktığı miras, akademik çevrelerde ve mühendislik uygulamalarında yaşamaya devam etmektedir.":
      "Mahir Vardar graduated from Istanbul Technical University as a mining engineer (MSc) in 1971 and worked as a research assistant at the Faculty of Civil Engineering of the Karlsruhe Institute of Technology until 1977, where he completed his doctorate. He then joined the ITU Faculty of Mines as a postdoctoral assistant, submitted his habilitation thesis in 1982 and became full professor in 1988. Having also served as head of department and dean, Vardar retired in 2017 and passed away on 3 May 2020. Working in mining, engineering geology, geomechanics, tunnelling and the design of rock structures, he contributed to numerous engineering projects and to the development of engineering services in Türkiye. Over more than forty years at ITU he trained generations of students, integrating his research and practical experience into his teaching. The importance he placed on addressing engineering problems on a scientific basis was reflected both in his professional work and in his relationship with his students. Respected for his knowledge, wisdom and wit, he is remembered as a versatile person who believed in science and valued his students. His joy of life, nourished by a love of people and nature, his professional expertise and the legacy of the students he trained live on in academia and in engineering practice.",
    "1937 yılında Bursa’da doğan Erdoğan Yüzer, İstanbul Üniversitesi Fen Fakültesi Jeofizik-Jeoloji Bölümünden mezun olmuştur. Yüksek lisansını İTÜ Hidrojeoloji Enstitüsünde, doktora ve doçentlik çalışmalarını İTÜ Maden Fakültesi Jeoloji Mühendisliği Bölümünde tamamlamış, 1977 yılında profesör olmuştur. Akademik yaşamı boyunca eğitim, araştırma ve yöneticilik görevlerini birlikte yürütmüş, üç dönem İTÜ Maden Fakültesi Dekanlığı yapmıştır. Mühendislik jeolojisi, hidrojeoloji, kaya mekaniği, geleneksel yapı malzemeleri ve çevre jeolojisi alanlarında çalışan Yüzer, İTÜ Maden, İnşaat ve Mimarlık Fakülteleri ile Fen Bilimleri Enstitüsünde dersler vermiştir. 1973–1982 yılları arasında Karadeniz Teknik, Ege ve İstanbul Üniversitelerinde de eğitim çalışmalarına katkıda bulunmuştur. 1983–1988 yılları arasında TÜBİTAK Temel Bilimler Araştırma Grubu üyeliği yapmış, Mühendislik Jeolojisi Türk Millî Komitesi Başkanlığı görevini üstlenmiştir. Türkçe ve İngilizce yayımlanan 130’dan fazla yayını ve beş kitabı bulunan Yüzer, bilimsel birikimini öğrencilerle ve meslek çevreleriyle paylaşmıştır. Uluslararası Mühendislik Jeolojisi Birliği, TMMOB Jeoloji Mühendisleri Odası ve Mühendislik Jeolojisi Derneğinin yaşam boyu onur üyesidir. Yurt Madenciliğini Geliştirme Vakfının kurucu başkanı olan hocamız, araştırmaları, yetiştirdiği öğrenciler ve mesleki kuruluşlara sunduğu katkılarla Türkiye’de mühendislik jeolojisinin gelişmesinde öncü bir rol üstlenmiştir.":
      "Born in Bursa in 1937, Erdoğan Yüzer graduated from the Department of Geophysics and Geology of the Faculty of Science, Istanbul University. He completed his master’s degree at the ITU Institute of Hydrogeology and his doctorate and habilitation at the Department of Geological Engineering of the ITU Faculty of Mines, becoming full professor in 1977. Throughout his academic career he combined teaching, research and administration, serving three terms as dean of the ITU Faculty of Mines. Working in engineering geology, hydrogeology, rock mechanics, traditional building materials and environmental geology, he taught at the ITU Faculties of Mines, Civil Engineering and Architecture and at the Graduate School of Science. Between 1973 and 1982 he also taught at Karadeniz Technical, Ege and Istanbul Universities. From 1983 to 1988 he was a member of the TÜBİTAK Basic Sciences Research Group and he chaired the Turkish National Committee of Engineering Geology. With more than 130 publications in Turkish and English and five books, he shared his knowledge with students and the profession. He is a lifetime honorary member of the International Association for Engineering Geology and the Environment, the Chamber of Geological Engineers of Türkiye and the Turkish Association of Engineering Geology. As founding president of the Turkish Mining Development Foundation, he played a pioneering role in the development of engineering geology in Türkiye through his research, his students and his contributions to professional organisations.",
    "1920 yılında doğan Kemal Erguvanlı, İstanbul Üniversitesindeki öğreniminin ardından doktorasını İstanbul Teknik Üniversitesinde tamamlamıştır. 1953 yılında İTÜ Maden Fakültesinin kuruluşunda görev almış, 1954–1957 yılları arasında Londra’daki Imperial College’da mühendislik jeolojisi ve rezervuar jeolojisi alanlarında araştırmalar yürütmüştür. Akademik yaşamı boyunca farklı fakültelerde verdiği derslerle bilgi ve deneyimlerini öğrencilerine aktarmıştır. Türkiye’de mühendislik jeolojisinin gelişmesine öncülük eden Erguvanlı, jeologların inşaat ve maden mühendisleri ile mimarlarla birlikte çalışmasının önemini vurgulamıştır. Yol, köprü, baraj ve yeraltı suyu projelerine sunduğu katkılarla bilimsel bilgiyi mühendislik uygulamalarıyla buluşturmuştur. Araştırmalarında ve eğitim çalışmalarında benimsediği disiplinler arası yaklaşım, farklı meslek gruplarının ortak bir anlayışla çalışmasına katkı sağlamıştır. İnsan ve doğa sevgisini mesleğine ve eğitim anlayışına yansıtan hocamız, yetiştirdiği öğrenciler ve uygulamaya dayanan bilimsel yaklaşımıyla kalıcı bir iz bırakmıştır. “Taş, toprak, su, işimiz bu!” sözü, mesleğe duyduğu bağlılığın ve yerbilimlerine bakışının bir ifadesi olarak kuşaktan kuşağa aktarılmaktadır.":
      "Born in 1920, Kemal Erguvanlı studied at Istanbul University and completed his doctorate at Istanbul Technical University. He took part in the founding of the ITU Faculty of Mines in 1953 and carried out research on engineering geology and reservoir geology at Imperial College London between 1954 and 1957. Throughout his academic career he passed on his knowledge and experience through the courses he taught at several faculties. A pioneer of engineering geology in Türkiye, Erguvanlı stressed the importance of geologists working together with civil and mining engineers and architects. Through his contributions to road, bridge, dam and groundwater projects he brought scientific knowledge together with engineering practice. The interdisciplinary approach he adopted in research and teaching helped different professions work with a shared understanding. Reflecting his love of people and nature in his profession and teaching, he left a lasting mark through his students and his practice-based scientific approach. His motto “Stone, soil, water – that is our job!” is passed down from generation to generation as an expression of his dedication to the profession and his view of the earth sciences.",
    "1892 yılında İstanbul Çamlıca’da doğan Ahmet Malik Sayar, matematik bilgini Salih Zeki Bey ile Vecihe Hanım’ın oğludur. Sultani Mektebindeki, bugünkü adıyla Galatasaray Lisesindeki öğreniminin ardından, Millî Eğitim Nezaretinin açtığı sınavı kazanarak jeoloji eğitimi almak üzere Fransa’ya gitmiştir. Lyon Üniversitesindeki öğrenimini tamamlayarak 1913 yılında yurda dönmüş, I. Dünya Savaşı sırasında Sina Cephesi’nde yedek subay olarak görev yapmıştır. 1918 yılında Darülfünunda asistan olarak akademik yaşamına başlayan Sayar, 1919 yılında doçent olmuş ve 1933 yılına kadar buradaki çalışmalarını sürdürmüştür. Bu dönemde Halkalı Ziraat Mektebinde de dersler vermiş, 1930’lu yıllarda çeşitli liselerde öğretmenlik yapmıştır. 1944 yılında İstanbul Teknik Üniversitesinin kurulmasıyla İnşaat Fakültesinde jeoloji profesörü olarak görev almış, Maden Fakültesinin kuruluşuna önemli katkılar sağlamıştır. 1953–1955 yılları arasında fakültenin dekanlığını yürütmüş, 1954 yılında ordinaryüs profesör unvanını almıştır. 1963 yılında emekli oluncaya kadar eğitim çalışmalarına devam etmiş, 11 Mart 1965 tarihinde aramızdan ayrılmıştır. Türkiye’de jeoloji eğitiminin gelişmesine öncülük eden Sayar, yetiştirdiği binlerce öğrencinin yanı sıra hazırladığı ders kitaplarıyla da kalıcı bir bilimsel miras bırakmıştır. Tevfik Gökmen ve Malik Ongan ile hazırladığı kitap, 1924–1950 yılları arasında Türkiye’de okutulan tek jeoloji ders kitabı olmuştur. Darülfünun ve üniversite öğrencileri için de eserler hazırlayan hocamız, özellikle omurgalı hayvan fosilleri üzerine yaptığı araştırmalarla Türkiye’de bu alandaki çalışmaların öncüleri arasında yer almıştır. Eğitim ve araştırmayı birlikte ele alan yaklaşımıyla, yerbilimlerinin ülkemizde kurumsallaşmasına ve yeni kuşaklara aktarılmasına önemli katkılar sunmuştur.":
      "Born in Çamlıca, Istanbul, in 1892, Ahmet Malik Sayar was the son of the mathematician Salih Zeki Bey and Vecihe Hanım. After studying at the Sultani School, today’s Galatasaray High School, he won a scholarship examination of the Ministry of Education and went to France to study geology. He completed his studies at the University of Lyon and returned home in 1913, serving as a reserve officer on the Sinai Front during the First World War. He began his academic career as an assistant at the Darülfünun in 1918, became associate professor in 1919 and continued his work there until 1933. During this period he also taught at the Halkalı School of Agriculture and, in the 1930s, at several high schools. With the establishment of Istanbul Technical University in 1944 he became professor of geology at the Faculty of Civil Engineering and made major contributions to the founding of the Faculty of Mines. He served as dean of the faculty from 1953 to 1955 and was awarded the title of ordinarius professor in 1954. He continued teaching until his retirement in 1963 and passed away on 11 March 1965. A pioneer of geology education in Türkiye, Sayar left a lasting scientific legacy through the thousands of students he trained and the textbooks he wrote. The book he prepared with Tevfik Gökmen and Malik Ongan was the only geology textbook taught in Türkiye between 1924 and 1950. He also wrote works for Darülfünun and university students and, through his research on vertebrate fossils in particular, was among the pioneers of the field in Türkiye. With an approach that combined teaching and research, he made important contributions to the institutionalisation of the earth sciences in Türkiye and to passing them on to new generations.",

    /* --- Kişiler --- */
    "Misafir Araştırmacılar ve Öğrenciler": "Visiting Researchers and Students",
    "Misafir Araştırmacılar": "Visiting Researchers",
    "Doktora ve Yüksek Lisans Öğrencileri": "PhD and MSc Students",
    "Lisans Öğrencileri": "Undergraduate Students",
    "Mezunlar": "Alumni",
    "Doktora": "PhD",
    "Yüksek Lisans": "MSc",
    "Lisans": "BSc",

    /* --- Projeler --- */
    "Devam Eden Projeler": "Ongoing Projects",
    "Tamamlanan Projeler": "Completed Projects",
    "Devam ediyor": "Ongoing",
    "Tamamlandı": "Completed",
    "İTÜ BAP – Hızlı Destek": "ITU BAP – Rapid Support",
    "İTÜ BAP – Araştırmaya Başlangıç": "ITU BAP – Research Initiation",
    "Yürütücü:": "Principal investigator:",
    "Araştırmacılar:": "Researchers:",
    "İstanbul'un Kültürel Miras Yapılarında Kullanılan Taşlar İçin Alternatif Kaynakların Belirlenmesine Yönelik Veri Tabanlı Uyumluluk İndeksi ve Deneysel Sistematiğin Geliştirilmesi":
      "Development of a Data-Driven Compatibility Index and Experimental Framework for Identifying Alternative Sources of Stones Used in Istanbul’s Cultural Heritage Structures",
    "▸ Proje kapsamında doktora, yüksek lisans ve lisans bursiyeri alınacaktır. Başvuru için:":
      "▸ PhD, MSc and undergraduate scholarship positions are available within the project. To apply:",
    "Sedimanter Kaya Malzemelerinde Çatlak Başlangıcı Gerilmesinin Parçacık Tabanlı Sayısal Modellemesinde Bağ Modellerinin Karşılaştırmalı Analizi":
      "Comparative Analysis of Bond Models in Particle-Based Numerical Modelling of Crack Initiation Stress in Sedimentary Rock Materials",
    "Sedimanter kaya malzemelerinde tek eksenli yükleme altındaki deneyler PFC tabanlı sayısal numunelerle simüle edilmekte; Parallel Bond ve Flat-Joint başta olmak üzere farklı bağ modelleri makro-mekanik parametrelere göre kalibre edilerek çatlak başlangıcı gerilmesini temsil etme başarıları karşılaştırılmaktadır. Çalışma, parçacık tabanlı modellemede bağ modeli seçimi için tekrarlanabilir bir değerlendirme yaklaşımı geliştirmeyi amaçlamaktadır.":
      "Uniaxial compression tests on sedimentary rock materials are simulated with PFC-based numerical specimens. Different bond models, mainly Parallel Bond and Flat-Joint, are calibrated against macro-mechanical parameters and compared in terms of how well they represent crack initiation stress. The study aims to develop a reproducible evaluation approach for selecting bond models in particle-based modelling.",
    "D-650 Karayolunun Arifiye-Bozüyük Kesimindeki Heyelan Tehlikesinin AHP ve CBS Tabanlı Yöntemlerle Değerlendirilmesi":
      "Assessment of Landslide Hazard along the Arifiye–Bozüyük Section of the D-650 Highway Using AHP and GIS-Based Methods",
    "Günlük 30.000’i aşkın taşıt trafiğine sahip D-650 Karayolu’nun Arifiye-Bozüyük kesiminde heyelan tehlikesi; eğim, litoloji, drenaj yoğunluğu ve topografik nemlilik gibi faktörlerin AHP ile ağırlıklandırılıp CBS ortamında birleştirilmesiyle haritalanmaktadır. Elde edilecek tehlike haritasının yol güvenliği ve bakım planlamasında karar vericilere bilimsel bir araç sunması hedeflenmektedir.":
      "Landslide hazard along the Arifiye–Bozüyük section of the D-650 Highway, which carries more than 30,000 vehicles per day, is being mapped by weighting factors such as slope, lithology, drainage density and topographic wetness with AHP and combining them in a GIS environment. The resulting hazard map is intended to provide decision-makers with a scientific tool for road safety and maintenance planning.",
    "İstanbul Kilinin Makaslama Parametrelerine Katkı Malzemelerinin Etkisinin Araştırılması":
      "Investigation of the Effect of Additives on the Shear Parameters of Istanbul Clay",
    "İstanbul’un batısındaki yüksek plastisiteli, düşük dayanımlı killerin iyileştirilmesinde bor endüstrisi atıklarının kullanılabilirliği araştırılmıştır. Farklı katkı oranları (%5, %7,5, %10) ve kür süreleri (7, 14, 21 gün) için makaslama dayanımı ve plastisite özelliklerindeki değişimler karşılaştırmalı olarak incelenmiştir.":
      "The usability of boron industry waste for improving the high-plasticity, low-strength clays in western Istanbul was investigated. Changes in shear strength and plasticity were compared for different additive ratios (5%, 7.5%, 10%) and curing times (7, 14, 21 days)."
  };

  var EK = {
    /* --- Ana sayfa --- */
    "İTÜ MADEN FAKÜLTESİ · JEOLOJİ MÜHENDİSLİĞİ BÖLÜMÜ": "ITU FACULTY OF MINES · DEPARTMENT OF GEOLOGICAL ENGINEERING",
    "Mühendislik Jeolojisi – Kaya Mekaniği – Hidrojeoloji Çalışma Grubu": "Engineering Geology – Rock Mechanics – Hydrogeology Working Group",
    "Kökleri İTÜ’de yerbilimleri eğitiminin kurulduğu yıllara uzanan grubumuz, kaya ve zeminlerin mühendislik davranışı, şev ve heyelan tehlikesi, yeraltı suyu ve kültürel miras yapı taşları üzerine deneysel, sayısal ve saha tabanlı araştırmalar yürütmektedir.":
      "With roots going back to the founding years of earth science education at ITU, our group carries out experimental, numerical and field-based research on the engineering behaviour of rocks and soils, slope and landslide hazards, groundwater and cultural heritage building stones.",
    "Dünden Bugüne MJKMH": "MJKMH Through the Years",
    "Kişiler": "People",
    "Makale": "Articles",
    "İlk %10’luk Dilimdeki Makale": "Articles in Top 10% Journals",
    "Q1 Makale": "Q1 Articles",
    "Proje": "Projects",
    "Araştırmacı": "Researchers",
    "Çalışma Alanlarımız": "Research Areas",
    "Mühendislik Jeolojisi": "Engineering Geology",
    "Kaya Mekaniği": "Rock Mechanics",
    "Hidrojeoloji": "Hydrogeology",
    "Heyelan ve kaya düşmesi tehlikesi, CBS tabanlı tehlike haritalaması, zemin iyileştirme ve altyapı projelerinde jeolojik değerlendirme.":
      "Landslide and rockfall hazard, GIS-based hazard mapping, ground improvement and geological assessment for infrastructure projects.",
    "Kayaçların dayanım ve deformasyon davranışı, çatlak başlangıcı, parçacık tabanlı sayısal modelleme, tünel ve şev stabilitesi.":
      "Strength and deformation behaviour of rocks, crack initiation, particle-based numerical modelling, tunnel and slope stability.",
    "Yeraltı suyu akımı ve kalitesi, kirletici taşınımı, akifer karakterizasyonu ve su–kaya etkileşimi.":
      "Groundwater flow and quality, contaminant transport, aquifer characterisation and water–rock interaction.",
    "Son Yayınlar": "Recent Publications",
    "Tüm yayınlar →": "All publications →",
    "Tüm projeler →": "All projects →",
    "Tüm haberler →": "All news →",
    "Haberler ve Duyurular": "News and Announcements",
    "Devamı →": "Read more →",
    "Görsel:": "Image:",
    "[Örnek] TÜBİTAK 1001 projemiz için bursiyer alımı başladı": "[Sample] Scholarship positions open in our TÜBİTAK 1001 project",
    "Kültürel miras yapı taşları projemizde görev alacak lisans, yüksek lisans ve doktora bursiyerleri aranıyor.":
      "We are looking for undergraduate, MSc and PhD scholars to join our cultural heritage building stones project.",
    "[Örnek] Arazi çalışması: İstanbul kazı şevlerinde ölçümler": "[Sample] Fieldwork: measurements on Istanbul excavation slopes",
    "Ekibimiz İstanbul’daki derin kazılarda süreksizlik ölçümleri ve numune alımı gerçekleştirdi.":
      "Our team carried out discontinuity measurements and sampling in deep excavations in Istanbul.",
    "[Örnek] EUROCK 2026’da iki bildiri sunduk": "[Sample] Two papers presented at EUROCK 2026",
    "Üsküp’te düzenlenen sempozyumda grubumuzun çalışmaları sözlü ve poster olarak sunuldu.":
      "Our group’s work was presented as oral and poster contributions at the symposium in Skopje.",
    "U.S. Department of Energy, kamu malı": "U.S. Department of Energy, public domain",
    /* --- Laboratuvarlar --- */
    "Örnek içerik.": "Sample content.",
    "Bu sayfa yerleşimi göstermek için hazırlanmıştır. Cihaz listesi, fotoğraflar ve sorumlu bilgileri güncellenecektir.":
      "This page has been prepared to show the layout. The equipment list, photographs and contact details will be updated.",
    "Çalışma grubumuz bünyesinde kaya mekaniği, indeks özellikler ve hidrojeoloji alanlarında üç laboratuvar bulunmaktadır. Laboratuvarlar lisans ve lisansüstü eğitimde, tez çalışmalarında ve araştırma projelerinde kullanılmaktadır.":
      "Our working group has three laboratories in rock mechanics, index properties and hydrogeology. The laboratories are used in undergraduate and graduate teaching, thesis work and research projects.",
    "Kaya Mekaniği Laboratuvarı": "Rock Mechanics Laboratory",
    "İndeks Özellikler Laboratuvarı": "Index Properties Laboratory",
    "Hidrojeoloji Laboratuvarı": "Hydrogeology Laboratory",
    "Kayaçların dayanım ve deformasyon özelliklerinin belirlendiği deneyler.": "Tests to determine the strength and deformation properties of rocks.",
    "Kaya ve zeminlerin fiziksel ve indeks özelliklerinin belirlenmesi.": "Determination of the physical and index properties of rocks and soils.",
    "Yeraltı suyu ölçümleri, su örneklemesi ve hidrolik iletkenlik deneyleri.": "Groundwater measurements, water sampling and hydraulic conductivity tests.",
    "Laboratuvarı incele →": "View laboratory →",
    "Konum:": "Location:",
    "İTÜ Ayazağa Kampüsü, Maden Fakültesi (bina ve oda bilgisi eklenecek)": "ITU Ayazağa Campus, Faculty of Mines (building and room to be added)",
    "Laboratuvarımızda kaya malzemesinin dayanım, deformasyon ve süreksizlik özelliklerini belirlemeye yönelik deneyler yapılmaktadır. Laboratuvar lisans ve lisansüstü derslerde, tez çalışmalarında ve araştırma projelerinde kullanılmaktadır.":
      "Our laboratory carries out tests to determine the strength, deformation and discontinuity properties of rock materials. It is used in undergraduate and graduate courses, thesis work and research projects.",
    "Laboratuvarımızda kaya ve zemin örneklerinin yoğunluk, porozite, su emme ve kıvam gibi indeks özellikleri belirlenmektedir. Bu deneyler mühendislik sınıflamalarının ve diğer deneylerin temelini oluşturur.":
      "Our laboratory determines index properties of rock and soil samples such as density, porosity, water absorption and consistency. These tests form the basis of engineering classifications and other tests.",
    "Laboratuvarımızda yeraltı suyu ve yüzey suyu örneklerinin fiziksel ve kimyasal özellikleri ile zemin ve kayaçların hidrolik iletkenliği belirlenmektedir. Arazi ölçüm ekipmanı saha çalışmalarında da kullanılmaktadır.":
      "Our laboratory determines the physical and chemical properties of groundwater and surface water samples and the hydraulic conductivity of soils and rocks. Field measurement equipment is also used in site investigations.",
    "Sorumlu öğretim üyesi:": "Faculty member in charge:",
    "İletişim:": "Contact:",
    "eklenecek": "to be added",
    "bina ve oda bilgisi eklenecek": "building and room to be added",
    "e-posta eklenecek": "e-mail to be added",
    "Yapılan Deneyler": "Tests",
    "Deney": "Test", "Standart": "Standard", "Cihaz": "Equipment",
    "Fotoğraflar": "Photographs", "Fotoğraf eklenecek": "Photo to be added",
    "Dış Hizmet": "External Services",
    "Laboratuvarımızda kurum dışı talepler için deney hizmeti verilip verilmediği ve başvuru süreci bu bölümde açıklanacaktır.":
      "Information on testing services for external requests and the application process will be provided in this section.",
    "← Tüm laboratuvarlar": "← All laboratories",
    "Tek eksenli basınç dayanımı ve deformabilite": "Uniaxial compressive strength and deformability",
    "Dolaylı (Brezilya) çekme dayanımı": "Indirect (Brazilian) tensile strength",
    "Nokta yükleme dayanım indeksi": "Point load strength index",
    "Schmidt çekici sertliği": "Schmidt hammer rebound hardness",
    "Suda dağılmaya karşı duraylılık": "Slake durability",
    "Ultrasonik ses hızı": "Ultrasonic wave velocity",
    "Süreksizlik makaslama dayanımı": "Shear strength of discontinuities",
    "Hidrolik pres, şekil değiştirme ölçerler": "Hydraulic press, strain gauges",
    "Hidrolik pres, Brezilya çeneleri": "Hydraulic press, Brazilian jaws",
    "Nokta yükleme cihazı": "Point load tester",
    "L tipi Schmidt çekici": "L-type Schmidt hammer",
    "Slake durability cihazı": "Slake durability apparatus",
    "P ve S dalgası ölçüm cihazı": "P- and S-wave measurement device",
    "Taşınabilir makaslama kutusu": "Portable shear box",
    "Birim hacim ağırlık, porozite ve su emme": "Unit weight, porosity and water absorption",
    "Özgül ağırlık": "Specific gravity",
    "Kıvam (Atterberg) limitleri": "Consistency (Atterberg) limits",
    "Dane boyu dağılımı": "Grain size distribution",
    "Su içeriği": "Water content",
    "Etüv, hassas terazi, vakum düzeneği": "Oven, precision balance, vacuum setup",
    "Piknometre": "Pycnometer",
    "Casagrande aleti": "Casagrande apparatus",
    "Elek takımı, sarsma makinesi": "Sieve set, sieve shaker",
    "Etüv, hassas terazi": "Oven, precision balance",
    "Hidrolik iletkenlik (sabit ve düşen seviyeli)": "Hydraulic conductivity (constant and falling head)",
    "Esnek çeperli permeabilite": "Flexible-wall permeability",
    "Arazi parametreleri (pH, EC, sıcaklık, çözünmüş oksijen)": "Field parameters (pH, EC, temperature, dissolved oxygen)",
    "Yeraltı suyu seviye ölçümü": "Groundwater level measurement",
    "Su örneklemesi": "Water sampling",
    "Permeametre düzenekleri": "Permeameter setups",
    "Esnek çeperli permeametre": "Flexible-wall permeameter",
    "Çok parametreli prob": "Multi-parameter probe",
    "Kuyu seviye ölçer, veri kaydedici": "Well level meter, data logger",
    "Bailer, örnekleme pompası": "Bailer, sampling pump",
    "Üretici yöntemleri": "Manufacturer methods",
    /* --- İletişim --- */
    "MJKMH Çalışma Grubu": "MJKMH Working Group",
    "Gizle": "Hide",
    "ADRES": "ADDRESS",
    "İstanbul Teknik Üniversitesi, Maden Fakültesi, Jeoloji Mühendisliği Bölümü, Sarıyer, İstanbul, Türkiye":
      "Istanbul Technical University, Faculty of Mines, Department of Geological Engineering, Sarıyer, Istanbul, Türkiye",
    "Tüm öğretim üyelerimizin iletişim bilgileri için": "For the contact details of all our faculty members, see the",
    "sayfasına bakabilirsiniz.": "page.",
    "ULAŞIM": "GETTING HERE",
    "M2 Yenikapı–Hacıosman metro hattının İTÜ-Ayazağa durağında inip kampüs içinden Maden Fakültesi’ne yürüyerek ulaşabilirsiniz.":
      "Take the M2 Yenikapı–Hacıosman metro line to İTÜ-Ayazağa station and walk through the campus to the Faculty of Mines.",
    /* --- Yayınlar --- */
    "Bildiri": "Conference Papers",
    "Derleme": "Review",
    "Kitap Bölümü": "Book Chapter",
    "İlk %10": "Top 10%",
    "Q değerleri Scopus CiteScore yüzdeliklerine göredir. Q değeri bulunmayan makaleler ve derlemeler sayılara katılmamıştır.":
      "Quartiles are based on Scopus CiteScore percentiles. Articles without a quartile and reviews are not included in the counts."
  };
  EK["İstanbul’un Kültürel Miras Yapılarında Kullanılan Taşlar İçin Alternatif Kaynakların Belirlenmesine Yönelik Veri Tabanlı Uyumluluk İndeksi ve Deneysel Sistematiğin Geliştirilmesi"] =
    TAM["İstanbul'un Kültürel Miras Yapılarında Kullanılan Taşlar İçin Alternatif Kaynakların Belirlenmesine Yönelik Veri Tabanlı Uyumluluk İndeksi ve Deneysel Sistematiğin Geliştirilmesi"];
  Object.keys(EK).forEach(function (k) { TAM[k] = EK[k]; });

  /* Parça değişimleri (uzundan kısaya uygulanır) */
  var PARCA = [
    ["Dr. Öğr. Üyesi", "Asst. Prof. Dr."],
    ["Arş. Gör. Dr.", "Res. Asst. Dr."],
    ["Arş. Gör.", "Res. Asst."],
    ["Doç. Dr.", "Assoc. Prof. Dr."],
    ["Teknisyen ", "Technician "],
    ["Post Doktora:", "Postdoc:"],
    ["Doktora Sırası:", "Visiting PhD:"],
    ["Doktora:", "PhD:"],
    ["Yüksek Lisans:", "MSc:"],
    ["Lisans:", "BSc:"],
    ["Danışman:", "Advisor:"],
    ["Proje No:", "Project No:"],
    ["(Yüksek Lisans)", "(MSc)"],
    ["(Doktora)", "(PhD)"],
    ["İstanbul Teknik Üniversitesi", "Istanbul Technical University"],
    ["İstanbul Üniversitesi", "Istanbul University"],
    ["Karadeniz Teknik Üniversitesi", "Karadeniz Technical University"],
    ["Kütahya Dumlupınar Üniversitesi", "Kütahya Dumlupınar University"],
    ["Kocaeli Üniversitesi", "Kocaeli University"],
    ["Çanakkale Onsekiz Mart Üniversitesi", "Çanakkale Onsekiz Mart University"],
    ["Hacettepe Üniversitesi", "Hacettepe University"],
    ["Akdeniz Üniversitesi", "Akdeniz University"],
    ["Ankara Üniversitesi", "Ankara University"],
    ["Orta Doğu Teknik Üniversitesi", "Middle East Technical University"],
    ["Dokuz Eylül Üniversitesi", "Dokuz Eylül University"],
    ["Süleyman Demirel Üniversitesi", "Süleyman Demirel University"],
    ["Selçuk Üniversitesi", "Selçuk University"],
    ["Yıldız Teknik Üniversitesi", "Yıldız Technical University"],
    ["Boğaziçi Üniversitesi", "Boğaziçi University"],
    ["Ege Üniversitesi", "Ege University"],
    ["Fırat Üniversitesi", "Fırat University"],
    ["Cumhuriyet Üniversitesi", "Cumhuriyet University"],
    ["Üniversitesi", "University"]
  ];

  var LINK = [
    ["/laboratuvar/kaya-mekanigi-laboratuvari", "/en/laboratories/rock-mechanics-laboratory"],
    ["/laboratuvar/indeks-ozellikler-laboratuvari", "/en/laboratories/index-properties-laboratory"],
    ["/laboratuvar/hidrojeoloji-laboratuvari", "/en/laboratories/hydrogeology-laboratory"],
    ["/laboratuvar", "/en/laboratories"],
    ["/hakkimizda", "/en/about-us"],
    ["/kisiler", "/en/people"],
    ["/yayinlar", "/en/publications"],
    ["/projeler", "/en/projects"],
    ["/haberler", "/en/news"],
    ["/iletisim", "/en/contact"]
  ];

  window.__cevir = function (html) {
    var kap = document.createElement('div');
    kap.innerHTML = html;
    var w = document.createTreeWalker(kap, NodeFilter.SHOW_TEXT), n, eksik = [];
    while ((n = w.nextNode())) {
      var ham = n.nodeValue, v = ham.trim();
      if (!v) continue;
      if (TAM.hasOwnProperty(v)) { n.nodeValue = ham.replace(v, TAM[v]); continue; }
      var y = ham;
      PARCA.forEach(function (p) { y = y.split(p[0]).join(p[1]); });
      n.nodeValue = y;
      if (/[çğıöşüÇĞİÖŞÜ]/.test(y) && /\s/.test(y.trim()) && y.trim().length > 25) eksik.push(y.trim().slice(0, 80));
    }
    kap.querySelectorAll('span.tag').forEach(function (sp) {
      var t = sp.textContent.trim(), tek = {"Articles": "Article", "Conference Papers": "Conference Paper"};
      if (tek[t]) sp.textContent = tek[t];
    });
    var w2 = document.createTreeWalker(kap, NodeFilter.SHOW_TEXT), m;
    while ((m = w2.nextNode())) {
      m.nodeValue = m.nodeValue
        .replace(/Kaynak: Scopus · Toplam (\d+) yayın · Son güncelleme: ([\d.]+)/, 'Source: Scopus · $1 publications in total · Last updated: $2');
    }
    kap.querySelectorAll('a[href]').forEach(function (a) {
      var h = a.getAttribute('href');
      if (/^\/haber-detay\//.test(h)) { a.setAttribute('href', '/en/news'); return; }
      for (var i = 0; i < LINK.length; i++) {
        if (h === LINK[i][0] || h.indexOf(LINK[i][0] + '/') === 0 || h.indexOf(LINK[i][0] + '#') === 0) {
          a.setAttribute('href', LINK[i][1] + h.slice(LINK[i][0].length)); break;
        }
      }
      if (/research\.itu\.edu\.tr\/tr\//.test(h)) a.setAttribute('href', h.replace('/tr/', '/en/'));
    });
    window.__eksik = eksik;
    return kap.innerHTML;
  };
})();
