# -*- coding: utf-8 -*-
"""Source unique du cours EIP (Cameroun) : Président de la République et Parlement.

Ce module ne contient que des données : la structure du document.
`build.py` en dérive le fichier LaTeX (cours_eip_cameroun.tex) et le PDF.

Types de blocs :
  ("chapter", titre)
  ("section", titre)
  ("subsection", titre)
  ("p", texte)
  ("ul", [items])
  ("ol", [items])
  ("table", [en-têtes], [[cellules]], [largeurs relatives])
  ("box", genre, titre, texte)            genre: key | warn | method | def
  ("qcm", [(question, [A, B, C])])
  ("dl", [(terme, définition)])

Balisage inline minimal : **gras**.  Pas de LaTeX brut dans les textes.
"""

DATE_MAJ = "17 septembre 2026"

SOURCES = [
    ("S1", "Constitution de la République du Cameroun (loi n° 96/06 du 18 janvier 1996 "
           "modifiant la Constitution du 2 juin 1972), texte officiel publié par l'Assemblée nationale",
     "https://www.assnat.cm/images/La_Constitution.pdf"),
    ("S2", "Loi n° 2008/001 du 14 avril 2008 modifiant et complétant certaines dispositions "
           "de la Constitution (articles 6, 14, 15, 51, 53 et 67)",
     "https://www.prc.cm/fr/le-cameroun/constitution"),
    ("S3", "Révision constitutionnelle du 4 avril 2026, promulguée le 14 avril 2026 : "
           "création du poste de Vice-Président (modification des articles 5, 6, 7, 10, 53 et 66)",
     "https://www.stopblablacam.com/politique/0504-16070-le-parlement-adopte-une-revision-constitutionnelle-creant-le-poste-de-vice-president-de-la-republique"),
    ("S4", "Digithèque MJP (université de Perpignan), texte consolidé de la Constitution "
           "camerounaise, révisions de 2008 et de 2026 signalées article par article",
     "https://mjp.univ-perp.fr/constit/cm2008.htm"),
    ("S5", "Assemblée nationale du Cameroun — organisation, bureau, commissions générales",
     "https://www.assnat.cm/index.php/fr/national-assembly/organisation"),
    ("S6", "Loi n° 2012/001 du 19 avril 2012 portant Code électoral, modifiée et complétée",
     "https://www.assnat.cm/images/lois-adoptees/code-electoral.pdf"),
    ("S7", "Sénat du Cameroun — présentation, composition, bureau, sessions et commissions",
     "https://senat.cm/?page_id=385"),
    ("S8", "Présidence de la République du Cameroun — rôle constitutionnel du Chef de l'État",
     "https://www.prc.cm/fr/le-president/role-constitutionnel"),
    ("S9", "AFP Factuel — vérification : aucun Vice-Président n'avait été nommé au moment "
           "de la diffusion d'un faux décret (avril 2026)",
     "https://factuel.afp.com/doc.afp.com.A7DJ2NQ"),
    ("S10", "Élection des présidents des deux chambres le 17 mars 2026 "
            "(Théodore Datouo à l'Assemblée nationale, Aboubakary Abdoulaye au Sénat)",
     "https://www.koaci.com/article/2026/03/17/cameroun/politique/cameroun-aboubakary-abdoulaye-nouveau-president-du-senat_195139.html"),
]

CONTENT = [

# ───────────────────────────── AVERTISSEMENT ─────────────────────────────
("chapter", "Avertissement et mode d'emploi"),

("p", "Ce document est un **support de préparation** au concours d'Élève Inspecteur de Police "
      "(EIP). Il n'est pas une consultation juridique. Toutes les règles exposées sont tirées "
      "de la Constitution de la République du Cameroun et des lois qui la modifient, ainsi que "
      "du Code électoral et des présentations officielles des deux chambres du Parlement. "
      "Les sources sont listées en fin de document et rappelées par des repères du type [S1]."),

("box", "warn", "Distinguer trois choses",
 "1. **La règle constitutionnelle** : elle ne change qu'avec une révision. C'est elle qui est "
 "évaluée au concours.\n"
 "2. **La règle légale** (Code électoral, règlements intérieurs) : elle précise la Constitution.\n"
 "3. **L'actualité** (noms des titulaires, composition politique) : elle change vite. "
 "Dans ce document, toute donnée d'actualité est **datée**. Arrêtée au " + DATE_MAJ + "."),

("box", "warn", "Réforme à ne pas manquer : la révision constitutionnelle de 2026",
 "Le Parlement réuni en Congrès a adopté le 4 avril 2026 une révision constitutionnelle "
 "promulguée le 14 avril 2026. Elle modifie les articles 5, 6, 7, 10, 53 et 66 et **crée le poste "
 "de Vice-Président de la République**, nommé par le Chef de l'État. Elle réorganise surtout "
 "la succession en cas de vacance de la Présidence. Les anciennes fiches qui présentent le "
 "Président du Sénat comme successeur automatique décrivent désormais un cas particulier "
 "et non plus le principe. [S3] [S4]"),

("section", "Ce que le candidat doit savoir faire"),
("ul", [
 "citer les articles constitutionnels essentiels sans confondre le texte de 1996, la révision "
 "de 2008 et celle de 2026 ;",
 "distinguer le Président de la République, le Vice-Président, le Gouvernement, "
 "l'Assemblée nationale, le Sénat et le Parlement ;",
 "expliquer l'élection et les pouvoirs du Chef de l'État, le bicamérisme, la navette "
 "législative, la promulgation et le contrôle parlementaire ;",
 "traiter une question de cours ou un QCM en justifiant chaque réponse par une règle précise ;",
 "relier ces connaissances au métier de police : légalité, hiérarchie des autorités, "
 "ordre public, respect des libertés.",
]),

# ───────────────────────────── FICHE EXPRESS ─────────────────────────────
("chapter", "Fiche express : les repères qui rapportent des points"),

("section", "Les vingt réponses à connaître par cœur"),
("table",
 ["Question", "Réponse exacte"],
 [
  ["Nature de l'État", "État unitaire décentralisé, un et indivisible, laïque, démocratique et social (art. 1er, al. 2)."],
  ["Langues officielles", "Le français et l'anglais, d'égale valeur (art. 1er, al. 3)."],
  ["Siège des institutions", "Yaoundé (art. 1er, al. 8)."],
  ["Autorité de l'État", "Exercée par le Président de la République et le Parlement (art. 4)."],
  ["Chef de l'État", "Le Président de la République (art. 5, al. 1)."],
  ["Durée du mandat présidentiel", "Sept ans ; le Président est rééligible (art. 6, al. 2, modifié en 2008)."],
  ["Mode d'élection du Président", "Suffrage universel direct, égal et secret, à la majorité des suffrages exprimés (art. 6, al. 1)."],
  ["Âge minimal du candidat à la Présidence", "Trente-cinq ans révolus à la date de l'élection, et être Camerounais d'origine."],
  ["Vice-Président", "Fonction créée en 2026 : nommé et révoqué par le Président ; ses pouvoirs procèdent d'une délégation expresse."],
  ["Succession depuis 2026", "En cas de vacance, le Vice-Président achève le mandat. À défaut (poste non pourvu ou Vice-Président empêché) : scrutin dans 20 à 120 jours, intérim par le Président du Sénat."],
  ["Composition du Parlement", "Deux chambres : l'Assemblée nationale et le Sénat (art. 14, al. 1)."],
  ["Missions du Parlement", "Légiférer et contrôler l'action du Gouvernement (art. 14, al. 2)."],
  ["Assemblée nationale", "180 députés, suffrage universel direct et secret, mandat de cinq ans (art. 15)."],
  ["Sénat", "100 sénateurs : 10 par région, dont 7 élus au suffrage indirect et 3 nommés par le Président (art. 20)."],
  ["Âge minimal du sénateur", "Quarante ans révolus à la date de l'élection ou de la nomination (art. 20, al. 3)."],
  ["Sessions ordinaires", "Trois par an, en mars, juin et novembre ; trente jours au maximum chacune."],
  ["Sessions extraordinaires", "Quinze jours au maximum, sur un ordre du jour déterminé."],
  ["Congrès", "Les deux chambres réunies : message du Président, serment des membres du Conseil constitutionnel, révision de la Constitution (art. 14, al. 4)."],
  ["Délai de promulgation", "Quinze jours à compter de la transmission, sauf seconde lecture ou saisine du Conseil constitutionnel (art. 31)."],
  ["Motion de censure", "Signée par au moins un tiers des députés ; adoptée à la majorité des deux tiers des membres composant l'Assemblée (art. 34, al. 3)."],
 ],
 [0.36, 0.64]),

("box", "key", "Deux formules-mémoire",
 "**Président : 5 – 6 – 7 – 8 – 9 – 10.** Article 5 (statut), 6 (élection et vacance), "
 "7 (serment), 8 (attributions), 9 (état d'urgence et état d'exception), 10 (nominations et délégations).\n"
 "**Parlement : 14 – 15 – 20 – 25 – 26 – 30 – 31 – 34 – 35.** Structure, Assemblée nationale, "
 "Sénat, initiative des lois, domaine de la loi, navette, promulgation, responsabilité du "
 "Gouvernement, contrôle parlementaire."),

("section", "Les sept pièges classiques"),
("ol", [
 "**« Le Président est élu pour sept ans renouvelable une fois » : faux aujourd'hui.** La loi "
 "n° 2008/001 du 14 avril 2008 a supprimé cette limitation ; le texte dit désormais « Il est "
 "rééligible ». [S2] [S4]",
 "**« Le Parlement, c'est l'Assemblée nationale » : faux.** Le Parlement est bicaméral ; le "
 "Sénat a été installé en 2013.",
 "**« Les sénateurs sont élus par tous les citoyens » : faux.** Sur dix sénateurs par région, "
 "sept sont élus au suffrage universel **indirect** et trois sont **nommés** par le Président.",
 "**« Le Président du Sénat est le successeur du Chef de l'État » : incomplet depuis 2026.** "
 "Il n'assure l'intérim que si le poste de Vice-Président n'est pas pourvu ou si le "
 "Vice-Président est lui-même empêché.",
 "**« Le Premier ministre est le Chef de l'État » : faux.** Il est le Chef du Gouvernement et "
 "dirige son action (art. 12).",
 "**« Le Président vote les lois » : faux.** Le Parlement vote la loi ; le Président la "
 "promulgue, peut demander une seconde lecture et peut saisir le Conseil constitutionnel.",
 "**« L'élection présidentielle se joue à deux tours » : faux.** Le scrutin est uninominal "
 "majoritaire **à un tour** : est élu le candidat qui obtient la majorité des suffrages "
 "exprimés. [S6]",
]),

# ───────────────────────────── CADRE CONSTITUTIONNEL ─────────────────────────────
("chapter", "Le cadre constitutionnel camerounais"),

("section", "La Constitution, norme suprême"),
("p", "La Constitution est la loi fondamentale de l'État : elle organise les pouvoirs publics, "
      "fixe leurs compétences et garantit les droits et libertés. Le texte de base est la "
      "Constitution du 2 juin 1972, révisée en profondeur par la **loi n° 96/06 du 18 janvier 1996**, "
      "puis modifiée par la **loi n° 2008/001 du 14 avril 2008** et par la **révision promulguée le "
      "14 avril 2026**. Il faut donc parler de la Constitution **en vigueur**, et non d'une "
      "« Constitution de 1996 » détachée de ses modifications. [S1] [S2] [S3]"),
("p", "Le préambule fait partie intégrante de la Constitution (art. 65). Il proclame notamment "
      "l'égalité en droits et en devoirs, la protection des minorités et des populations "
      "autochtones, la liberté et la sécurité individuelles, l'inviolabilité du domicile et du "
      "secret des correspondances, la non-rétroactivité de la loi, la présomption d'innocence, "
      "l'interdiction de la torture et des traitements cruels, inhumains ou dégradants, la "
      "laïcité de l'État, les libertés de communication, d'expression, de presse, de réunion, "
      "d'association et le droit de grève, le droit à l'instruction, le droit de propriété, le "
      "droit à un environnement sain, ainsi que le devoir de contribuer aux charges publiques "
      "et à la défense de la patrie."),

("box", "def", "Trois notions à ne pas confondre",
 "**Constitution** : norme suprême, révisable selon la procédure des articles 63 et 64.\n"
 "**Loi** : texte voté par le Parlement dans les matières de l'article 26.\n"
 "**Règlement** : acte de l'exécutif dans toutes les matières qui ne relèvent pas de la loi (art. 27)."),

("section", "Les principes de l'État"),
("ul", [
 "**Unitaire** : il n'existe pas d'États fédérés ; l'autorité constitutionnelle est unique.",
 "**Décentralisé** : les régions et les communes sont des collectivités territoriales "
 "décentralisées, personnes morales de droit public dotées de l'autonomie administrative et "
 "financière (art. 55).",
 "**Un et indivisible** : l'unité du territoire et de la Nation est protégée ; aucune révision "
 "ne peut y porter atteinte (art. 64).",
 "**Laïque** : l'État est neutre et indépendant à l'égard de toutes les religions ; la liberté "
 "de culte est garantie.",
 "**Démocratique et social** : la souveraineté nationale appartient au peuple, qui l'exerce par "
 "l'intermédiaire du Président de la République et des membres du Parlement, ou par voie de "
 "référendum (art. 2, al. 1).",
 "**Bilingue** : le français et l'anglais ont le même statut ; l'État garantit la promotion du "
 "bilinguisme et œuvre à la protection des langues nationales.",
]),

("section", "La souveraineté, le vote et les partis"),
("p", "Les autorités chargées de diriger l'État tiennent leurs pouvoirs du peuple par voie "
      "d'élections au suffrage universel direct ou indirect, sauf disposition contraire de la "
      "Constitution (art. 2, al. 2). Le vote est **égal et secret** ; y participent tous les "
      "citoyens âgés d'au moins **vingt ans** (art. 2, al. 3). Les partis et formations "
      "politiques concourent à l'expression du suffrage ; ils doivent respecter les principes de "
      "la démocratie, de la souveraineté et de l'unité nationales (art. 3)."),

("box", "def", "Suffrage direct et suffrage indirect",
 "**Direct** : l'électeur désigne lui-même le titulaire du mandat (Président de la République, "
 "député).\n"
 "**Indirect** : l'électeur désigne des grands électeurs qui élisent à leur tour "
 "(les 70 sénateurs élus le sont par les conseillers régionaux et municipaux)."),

("section", "La carte des institutions"),
("p", "L'article 4 énonce que l'autorité de l'État est exercée par le Président de la République "
      "et par le Parlement. La Constitution organise ensuite le pouvoir exécutif (titre II), le "
      "pouvoir législatif (titre III), les rapports entre eux (titre IV), le pouvoir judiciaire "
      "(titre V), les traités (titre VI), le Conseil constitutionnel (titre VII), la Haute Cour "
      "de justice (titre VIII), le Conseil économique et social (titre IX) et les collectivités "
      "territoriales décentralisées (titre X)."),

("table",
 ["Institution", "Fonction", "Articles"],
 [
  ["Président de la République", "Chef de l'État, clé de voûte de l'exécutif", "5 à 10"],
  ["Vice-Président", "Assiste le Président ; achève le mandat en cas de vacance", "5, 6, 7, 10 (révision 2026)"],
  ["Gouvernement / Premier ministre", "Met en œuvre la politique de la Nation", "11 à 13"],
  ["Assemblée nationale", "Représente la Nation ; vote la loi et le budget", "15 à 19"],
  ["Sénat", "Représente les collectivités territoriales décentralisées", "20 à 24"],
  ["Pouvoir judiciaire", "Cour suprême, cours d'appel, tribunaux", "37 à 42"],
  ["Conseil constitutionnel", "Constitutionnalité, régulation, élections", "46 à 52"],
  ["Haute Cour de justice", "Haute trahison, complot contre la sûreté de l'État", "53"],
  ["Conseil économique et social", "Organe consultatif", "54"],
  ["Régions et communes", "Collectivités territoriales décentralisées", "55 à 62"],
 ],
 [0.30, 0.46, 0.24]),

("box", "method", "Réflexe de copie",
 "Commencer par la base juridique : « Selon l'article … de la Constitution… », puis seulement "
 "expliquer la portée pratique. Une réponse politique ou journalistique ne répond pas à une "
 "question de droit."),

# ───────────────────────────── PRÉSIDENT ─────────────────────────────
("chapter", "Le Président de la République"),

("section", "Statut et rôle constitutionnel (article 5)"),
("p", "Le Président de la République est le **Chef de l'État**. Élu de la Nation tout entière, "
      "il incarne l'unité nationale. Il **définit la politique de la Nation**, veille au respect "
      "de la Constitution et assure, par son arbitrage, le fonctionnement régulier des pouvoirs "
      "publics. Il est le **garant** de l'indépendance nationale, de l'intégrité du territoire, "
      "de la permanence et de la continuité de l'État, ainsi que du respect des traités et "
      "accords internationaux. [S1] [S8]"),
("p", "Depuis la révision de 2026, l'article 5 ajoute que le Président **peut être assisté d'un "
      "Vice-Président**. Cette assistance ne retire au Chef de l'État aucune de ses prérogatives : "
      "il demeure notamment Chef des Forces armées. [S4]"),
("p", "Cette position fait du Président la clé de voûte de l'exécutif, sans supprimer les "
      "compétences propres du Parlement, du Gouvernement, du Conseil constitutionnel et du "
      "pouvoir judiciaire. Le Président n'est pas le Gouvernement : le Gouvernement **met en "
      "œuvre** la politique que le Président **définit**, et il est responsable devant "
      "l'Assemblée nationale."),

("section", "Élection, mandat et entrée en fonction (articles 6 et 7)"),
("subsection", "Les règles constitutionnelles"),
("ul", [
 "**Mode de scrutin** : suffrage universel **direct, égal et secret**, à la majorité des "
 "suffrages exprimés (art. 6, al. 1). Le Code électoral en fait un scrutin uninominal "
 "majoritaire **à un tour**. [S6]",
 "**Durée** : sept ans. Depuis 2008, le Président **est rééligible**, sans limitation du nombre "
 "de mandats (art. 6, al. 2).",
 "**Date** : l'élection a lieu vingt jours au moins et cinquante jours au plus avant "
 "l'expiration des pouvoirs du Président en exercice (art. 6, al. 3).",
 "**Conditions de candidature** : être citoyen camerounais **d'origine**, jouir de ses droits "
 "civiques et politiques et avoir **trente-cinq ans révolus** à la date de l'élection.",
 "**Renvoi à la loi** : le régime de l'élection présidentielle est fixé par la loi, "
 "c'est-à-dire par le Code électoral.",
]),
("p", "Le Code électoral ajoute les conditions de dossier et de procédure : inscription sur une "
      "liste électorale, résidence continue sur le territoire national pendant au moins douze "
      "mois, investiture par un parti politique ou, pour une candidature indépendante, "
      "présentation par trois cents personnalités originaires de toutes les régions, à raison de "
      "trente par région, ainsi que le versement d'un cautionnement. [S6]"),

("subsection", "Prestation de serment (article 7)"),
("p", "Le Président élu **entre en fonction dès sa prestation de serment**. Il prête serment "
      "devant le peuple camerounais, en présence des membres du Parlement, du Conseil "
      "constitutionnel et de la Cour suprême réunis en séance solennelle. Le serment est **reçu "
      "par le Président de l'Assemblée nationale**. Les fonctions de Président de la République "
      "— et, depuis 2026, celles de Vice-Président — sont incompatibles avec toute autre fonction "
      "publique élective et avec toute activité professionnelle."),

("subsection", "Repère d'actualité (donnée datée)"),
("p", "À la date du " + DATE_MAJ + ", le Président de la République est **Son Excellence Paul BIYA**, "
      "en fonction depuis le 6 novembre 1982 et investi pour un nouveau mandat après l'élection "
      "présidentielle de 2025. Ce nom est une donnée d'actualité : au concours, c'est la règle de "
      "l'article 6 qui est attendue, le nom ne venant qu'en illustration."),

("section", "Les attributions du Président (article 8)"),
("ol", [
 "**Représentation** : il représente l'État dans tous les actes de la vie publique.",
 "**Forces armées** : il est le Chef des Forces armées.",
 "**Sécurité** : il veille à la sécurité intérieure et extérieure de la République.",
 "**Diplomatie** : il accrédite les ambassadeurs et les envoyés extraordinaires auprès des "
 "puissances étrangères ; ceux des puissances étrangères sont accrédités auprès de lui.",
 "**Promulgation** : il promulgue les lois dans les conditions de l'article 31.",
 "**Saisine du Conseil constitutionnel** : il le saisit dans les conditions prévues par la "
 "Constitution.",
 "**Droit de grâce** : il l'exerce après avis du Conseil supérieur de la magistrature.",
 "**Pouvoir réglementaire** : il l'exerce dans les matières qui ne relèvent pas du domaine de "
 "la loi.",
 "**Services publics** : il crée et organise les services publics de l'État.",
 "**Nominations** : il nomme aux emplois civils et militaires de l'État.",
 "**Décorations** : il confère les décorations et distinctions honorifiques de la République.",
 "**Dissolution** : en cas de nécessité, après consultation du Gouvernement et des bureaux de "
 "l'Assemblée nationale et du Sénat, il peut prononcer la dissolution de l'Assemblée nationale ; "
 "l'élection d'une nouvelle Assemblée se fait alors selon l'article 15, alinéa 4.",
]),

("box", "key", "Grâce et amnistie",
 "La **grâce** est une mesure individuelle du Président qui dispense de tout ou partie de "
 "l'exécution d'une peine : la condamnation subsiste. L'**amnistie** efface l'infraction "
 "elle-même et relève du **domaine de la loi** (art. 26, al. 2, c, 6). Ne jamais les confondre."),

("section", "Les pouvoirs de crise (article 9)"),
("subsection", "L'état d'urgence"),
("p", "Lorsque les circonstances l'exigent, le Président peut **proclamer par décret l'état "
      "d'urgence**, qui lui confère des pouvoirs spéciaux **dans les conditions fixées par la "
      "loi**. Trois éléments à retenir : un décret présidentiel, des circonstances qui l'exigent, "
      "des pouvoirs spéciaux encadrés par la loi."),
("subsection", "L'état d'exception"),
("p", "En cas de **péril grave** menaçant l'intégrité du territoire, la vie, l'indépendance ou "
      "les institutions de la République, le Président peut **proclamer par décret l'état "
      "d'exception** et prendre toutes les mesures qu'il juge nécessaires. Il en **informe la "
      "Nation par voie de message**."),

("table",
 ["Critère", "État d'urgence", "État d'exception"],
 [
  ["Fondement", "Article 9, alinéa 1", "Article 9, alinéa 2"],
  ["Déclencheur", "Les circonstances l'exigent", "Péril grave pour le territoire, la vie, l'indépendance ou les institutions"],
  ["Forme", "Décret du Président", "Décret du Président"],
  ["Effet", "Pouvoirs spéciaux dans les conditions fixées par la loi", "Toutes mesures jugées nécessaires"],
  ["Information", "Non prévue par le texte", "Message à la Nation"],
 ],
 [0.20, 0.38, 0.42]),

("box", "warn", "Portée pour un policier",
 "Ni l'état d'urgence ni l'état d'exception ne suspendent l'obligation de légalité. Les forces "
 "de sécurité restent soumises à la Constitution, aux lois et aux règlements, et un ordre "
 "manifestement illégal n'est jamais couvert par le régime de crise."),

("section", "Le Président, le Vice-Président et le Gouvernement (article 10)"),
("subsection", "Nominations et délégations"),
("p", "Selon l'article 10 tel que révisé en 2026, le Président de la République **nomme le "
      "Vice-Président, le Premier ministre et, sur proposition de ce dernier, les autres membres "
      "du Gouvernement**. Il fixe leurs attributions, met fin à leurs fonctions et préside les "
      "conseils ministériels. Le Vice-Président n'est donc **pas élu** : il est nommé, et il peut "
      "être révoqué par le Président. La durée de ses fonctions ne peut excéder celle du mandat "
      "présidentiel en cours. [S3] [S4]"),
("p", "Le Président peut **déléguer certains de ses pouvoirs** au Vice-Président, au Premier "
      "ministre, aux autres membres du Gouvernement et à certains hauts responsables de "
      "l'administration, dans le cadre de leurs attributions respectives. En cas d'empêchement "
      "temporaire, il charge le Vice-Président, le Premier ministre ou, à défaut, un autre "
      "membre du Gouvernement d'assurer certaines de ses fonctions **dans le cadre d'une "
      "délégation expresse**."),

("subsection", "Le Gouvernement et le Premier ministre (articles 11 à 13)"),
("ul", [
 "Le Gouvernement est chargé de la **mise en œuvre de la politique de la Nation telle que "
 "définie par le Président** ; il est responsable devant l'Assemblée nationale dans les "
 "conditions de l'article 34 (art. 11).",
 "Le **Premier ministre est le Chef du Gouvernement** et dirige son action ; il est chargé de "
 "l'exécution des lois ; il exerce le pouvoir réglementaire et nomme aux emplois civils, sous "
 "réserve des prérogatives du Président ; il dirige les services administratifs nécessaires à "
 "sa mission et peut déléguer certains de ses pouvoirs (art. 12).",
 "Les fonctions de membre du Gouvernement sont **incompatibles** avec tout mandat parlementaire, "
 "avec la présidence d'un exécutif ou d'une assemblée de collectivité territoriale "
 "décentralisée, avec toute fonction de représentation professionnelle à caractère national et "
 "avec tout emploi ou activité professionnelle (art. 13).",
]),

("section", "La vacance de la Présidence : le droit applicable depuis 2026"),
("p", "La révision de 2026 a réorganisé l'article 6. Il faut désormais raisonner en **deux "
      "scénarios**, et n'invoquer le Président du Sénat que dans le second."),

("table",
 ["Situation", "Mécanisme applicable"],
 [
  ["Vacance par décès, démission ou empêchement définitif constaté par le Conseil constitutionnel, **un Vice-Président étant en fonctions**",
   "Le Vice-Président **achève le mandat** du Président de la République. Il prête serment dès l'ouverture de la vacance, dans les termes et conditions fixés par la loi (art. 7, al. 4 nouveau)."],
  ["**Vice-Président empêché ou poste non pourvu**",
   "Un scrutin est organisé pour élire un nouveau Président **vingt jours au moins et cent vingt jours au plus** après l'ouverture de la vacance. L'intérim est exercé de plein droit par le **Président du Sénat** ou, s'il est empêché, par son suppléant suivant l'ordre de préséance du Sénat."],
  ["Limites de l'intérim",
   "Le Président par intérim ne peut modifier ni la Constitution ni la composition du Gouvernement, ne peut recourir au référendum et **ne peut être candidat** à l'élection organisée. Exception : si l'organisation de l'élection l'exige, il peut modifier la composition du Gouvernement après consultation du Conseil constitutionnel."],
 ],
 [0.34, 0.66]),

("box", "warn", "Ne jamais inventer de titulaire",
 "La révision de 2026 **crée** la fonction de Vice-Président et donne au Président le pouvoir de "
 "la pourvoir ; elle ne prouve pas à elle seule qu'une personne a été nommée. De faux décrets de "
 "nomination ont circulé en avril 2026 et ont été démentis. [S9] Ne retenir un nom qu'après "
 "publication d'un acte présidentiel authentique au Journal officiel."),

("section", "Responsabilité, Haute Cour de justice et déclaration des biens"),
("p", "La **Haute Cour de justice** (art. 53) est compétente pour juger les actes accomplis dans "
      "l'exercice de leurs fonctions par le Président de la République **en cas de haute "
      "trahison**, et — depuis la révision de 2026 — par le **Vice-Président**, le Premier "
      "ministre, les autres membres du Gouvernement et assimilés, ainsi que les hauts "
      "responsables de l'administration ayant reçu délégation de pouvoirs en application des "
      "articles 10 et 12, **en cas de complot contre la sûreté de l'État**."),
("p", "Le Président de la République ne peut être mis en accusation que par l'Assemblée nationale "
      "et le Sénat statuant **par un vote identique, au scrutin public, à la majorité des quatre "
      "cinquièmes** des membres les composant. Les actes accomplis par le Président en "
      "application des articles 5, 8, 9 et 10 sont couverts par l'immunité et ne sauraient "
      "engager sa responsabilité à l'issue de son mandat."),
("p", "L'article 66, complété en 2026, impose une **déclaration des biens et avoirs au début et à "
      "la fin du mandat ou de la fonction** au Président de la République, au Vice-Président, au "
      "Premier ministre, aux membres du Gouvernement et assimilés, aux membres des bureaux des "
      "deux chambres, aux députés et sénateurs, à tout détenteur d'un mandat électif, aux "
      "secrétaires généraux de ministères, aux directeurs d'administration centrale, aux "
      "directeurs généraux des entreprises publiques et parapubliques, aux magistrats et à tout "
      "gestionnaire de crédits et de biens publics."),

("box", "key", "Deux responsabilités à distinguer",
 "**Responsabilité pénale devant la Haute Cour de justice** : elle vise le Président (haute "
 "trahison) et, depuis 2026, le Vice-Président et les membres du Gouvernement (complot contre "
 "la sûreté de l'État).\n"
 "**Responsabilité politique devant l'Assemblée nationale** : elle ne vise que le Gouvernement, "
 "par la question de confiance et la motion de censure (art. 34). Le Président, lui, n'est pas "
 "politiquement responsable devant le Parlement."),

("section", "Le Président de la République et le métier de police"),
("ul", [
 "Le Chef de l'État veille à la sécurité intérieure et extérieure : la police participe à cette "
 "mission constitutionnelle, mais dans le cadre de la loi.",
 "Savoir identifier l'autorité compétente et le texte qui fonde chaque acte : Chef de l'État, "
 "Gouvernement, autorité administrative (préfet, délégué du Gouvernement) ou autorité judiciaire.",
 "Protéger l'ordre public sans méconnaître la dignité de la personne, la présomption "
 "d'innocence et les droits de la défense, garantis par le préambule.",
 "Comprendre que l'état d'urgence et l'état d'exception reposent sur un cadre constitutionnel "
 "et légal, et non sur une permission générale.",
 "Rédiger des actes et comptes rendus précis, datés, factuels et juridiquement qualifiés.",
]),

# ───────────────────────────── PARLEMENT ─────────────────────────────
("chapter", "Le Parlement : règles communes aux deux chambres"),

("section", "Définition et missions (article 14)"),
("p", "Le **pouvoir législatif est exercé par le Parlement**, qui comprend deux chambres : "
      "l'Assemblée nationale et le Sénat. Le Parlement **légifère et contrôle l'action du "
      "Gouvernement**. Le bicamérisme signifie que deux chambres participent au travail "
      "législatif, avec des modes de représentation différents : la Nation pour l'Assemblée "
      "nationale, les collectivités territoriales décentralisées pour le Sénat."),

("box", "def", "Vocabulaire exact",
 "**Parlement** = Assemblée nationale + Sénat.\n"
 "**Gouvernement** = organe chargé de mettre en œuvre la politique de la Nation ; ce n'est pas "
 "une chambre.\n"
 "**Congrès** = réunion des deux chambres dans les cas limitativement prévus ; ce n'est pas une "
 "troisième chambre permanente.\n"
 "**Législature** = durée du mandat collectif de l'Assemblée nationale."),

("section", "Les sessions"),
("p", "Les chambres du Parlement se réunissent **aux mêmes dates** : en sessions ordinaires, "
      "chaque année aux mois de **mars, juin et novembre**, sur convocation des bureaux de "
      "l'Assemblée nationale et du Sénat après consultation du Président de la République ; en "
      "sessions extraordinaires, à la demande du Président de la République ou du tiers des "
      "membres composant l'une et l'autre chambres. Les deux chambres ne sont convoquées "
      "simultanément que si les matières portées à l'ordre du jour concernent l'une et l'autre "
      "(art. 14, al. 3, modifié en 2008)."),
("ul", [
 "Chaque chambre tient **trois sessions ordinaires par an**, de **trente jours au maximum** "
 "chacune (art. 16 et 21).",
 "Une **session extraordinaire** dure **quinze jours au maximum**, se tient sur un **ordre du "
 "jour déterminé** et est close dès l'épuisement de cet ordre du jour.",
 "Au début de chaque législature, chaque chambre se réunit **de plein droit** en session "
 "ordinaire, dans les conditions fixées par la loi.",
 "À l'ouverture de sa première session ordinaire, chaque chambre **élit son président et son "
 "bureau**.",
]),

("section", "Le Congrès (article 14, alinéa 4)"),
("p", "Les deux chambres peuvent se réunir en Congrès **à la demande du Président de la "
      "République** :"),
("ol", [
 "pour entendre une communication ou recevoir un **message** du Président de la République ;",
 "pour recevoir le **serment des membres du Conseil constitutionnel** ;",
 "pour se prononcer sur un projet ou une proposition de **révision constitutionnelle**.",
]),
("p", "Lorsque le Parlement se réunit en Congrès, c'est le **bureau de l'Assemblée nationale** "
      "qui préside les débats. C'est en Congrès qu'a été adoptée, le 4 avril 2026, la révision "
      "créant la Vice-Présidence. [S3]"),

("section", "Séances, ordre du jour et statut des parlementaires"),
("ul", [
 "Les **séances sont publiques**. À la demande du Gouvernement ou de la majorité absolue de ses "
 "membres, une chambre peut exceptionnellement se réunir **à huis clos** (art. 17 et 22).",
 "Chaque chambre fixe elle-même ses règles d'organisation et de fonctionnement sous forme de "
 "**loi portant règlement intérieur**, soumise au contrôle du Conseil constitutionnel avant "
 "mise en application.",
 "L'**ordre du jour** est fixé par la **conférence des présidents**, qui comprend les présidents "
 "des groupes parlementaires, les présidents des commissions et les membres du bureau ; un "
 "membre du Gouvernement y participe (art. 18 et 23).",
 "Sont **irrecevables** les propositions de loi et amendements qui entraîneraient une diminution "
 "des ressources publiques ou une aggravation des charges publiques sans compensation "
 "équivalente. En cas de doute, le Conseil constitutionnel tranche.",
 "L'ordre du jour comporte **en priorité** les projets de loi et les propositions acceptées par "
 "le Gouvernement, dans l'ordre qu'il a fixé. L'**urgence est de droit** lorsque le Gouvernement "
 "la demande.",
 "**Nul ne peut appartenir à la fois à l'Assemblée nationale et au Sénat** (art. 14, al. 5). La "
 "loi fixe le régime électoral des deux chambres ainsi que les immunités, inéligibilités, "
 "incompatibilités, indemnités et privilèges des parlementaires.",
]),

# ───────────────────────────── ASSEMBLÉE NATIONALE ─────────────────────────────
("chapter", "L'Assemblée nationale"),

("section", "Composition et mandat (article 15)"),
("ul", [
 "**180 députés** élus au suffrage universel **direct et secret** pour un mandat de **cinq ans**. "
 "Le nombre de députés peut être modifié par la loi.",
 "**Chaque député représente l'ensemble de la Nation** : il n'est pas le mandataire de sa seule "
 "circonscription.",
 "**Tout mandat impératif est nul** : aucune instruction juridiquement contraignante ne peut lui "
 "être imposée.",
 "En cas de crise grave ou lorsque les circonstances l'exigent, le Président de la République "
 "peut, après consultation du Président du Conseil constitutionnel et des bureaux des deux "
 "chambres, demander à l'Assemblée de décider **par une loi** de **proroger ou d'abréger son "
 "mandat**. L'élection d'une nouvelle Assemblée a lieu **quarante jours au moins et cent vingt "
 "jours au plus** après l'expiration du délai de prorogation ou d'abrègement (alinéa modifié en 2008).",
]),
("p", "Le Code électoral prévoit qu'est éligible à l'Assemblée nationale le citoyen camerounais "
      "jouissant du droit de vote, inscrit sur une liste électorale, âgé de **vingt-trois ans "
      "révolus** à la date du scrutin et sachant lire et écrire le français ou l'anglais, sous "
      "réserve des inéligibilités et incompatibilités légales. L'élection se fait au scrutin de "
      "liste dans les circonscriptions à plusieurs sièges et au scrutin uninominal majoritaire "
      "à un tour là où il n'y a qu'un siège à pourvoir. [S6]"),

("box", "def", "Le système mixte des circonscriptions plurinominales",
 "Si une liste obtient la **majorité absolue** des suffrages exprimés, elle emporte **tous** les "
 "sièges. Sinon, la liste arrivée en tête reçoit la **moitié** des sièges (arrondie à l'entier "
 "supérieur) et l'autre moitié est répartie **à la proportionnelle** entre toutes les listes "
 "ayant franchi le seuil légal, y compris celle arrivée en tête. [S6]"),

("section", "Organisation interne"),
("subsection", "Le bureau"),
("p", "Au début de chaque législature, puis à l'ouverture de la première session ordinaire de "
      "chaque année, l'Assemblée nationale élit son Président et les membres de son bureau. "
      "La présentation officielle de l'Assemblée fait état d'un Président, d'un premier "
      "Vice-Président, de cinq Vice-Présidents, de quatre Questeurs et de douze Secrétaires, le "
      "Secrétaire général de l'Assemblée étant membre de droit et conseiller juridique et "
      "parlementaire. [S5]"),
("subsection", "La conférence des présidents"),
("p", "Elle réunit le Président de l'Assemblée, les membres du bureau, les présidents des "
      "commissions générales et les présidents des groupes parlementaires, avec la participation "
      "d'un membre du Gouvernement. Elle prépare l'ordre du jour, examine la recevabilité des "
      "textes, les renvoie aux commissions compétentes et fixe le calendrier des séances "
      "plénières."),
("subsection", "Les neuf commissions générales"),
("ol", [
 "Commission des lois constitutionnelles, des droits de l'homme et des libertés, de la justice, "
 "de la législation et du règlement, de l'administration ;",
 "Commission des finances et du budget ;",
 "Commission des affaires étrangères ;",
 "Commission de la défense nationale et de la sécurité ;",
 "Commission des affaires économiques, de la programmation et de l'aménagement du territoire ;",
 "Commission de l'éducation, de la formation professionnelle et de la jeunesse ;",
 "Commission des affaires culturelles, sociales et familiales ;",
 "Commission de la production et des échanges ;",
 "Commission des résolutions et des pétitions. [S5]",
]),

("section", "Compétences propres"),
("ul", [
 "**Voter la loi** à la **majorité simple** des députés (art. 19, al. 1).",
 "**Voter le budget de l'État** au cours de l'une de ses sessions. Si le budget n'est pas adopté "
 "avant la fin de l'année budgétaire, le Président de la République est habilité à reconduire "
 "**par douzièmes** le budget de l'exercice précédent jusqu'à l'adoption du nouveau (art. 16, al. 2, b).",
 "**Adopter ou rejeter** les textes soumis à son réexamen par le Sénat, selon l'article 30.",
 "Statuer sur les lois soumises à **seconde lecture** par le Président de la République : elles "
 "sont alors adoptées à la **majorité absolue** des députés (art. 19, al. 3).",
 "**Mettre en cause la responsabilité du Gouvernement** par la motion de censure (art. 34).",
 "Concourir, avec le Sénat, à la **mise en accusation** du Président de la République devant la "
 "Haute Cour de justice (art. 53).",
]),

("box", "method", "Erreur fréquente",
 "Ne pas réduire l'Assemblée nationale au vote des lois : elle vote aussi le budget, contrôle le "
 "Gouvernement, participe à la navette avec le Sénat, crée des commissions d'enquête et "
 "intervient dans la mise en accusation du Chef de l'État."),

("subsection", "Repère d'actualité (donnée datée)"),
("p", "Le 17 mars 2026, l'Assemblée nationale a élu **Théodore DATOUO** à sa présidence, mettant "
      "fin à trente-quatre ans de présidence de Cavayé Yéguié Djibril. [S10] Donnée arrêtée au "
      + DATE_MAJ + " : la composition politique et les titulaires peuvent évoluer, contrairement "
      "à la règle constitutionnelle des 180 sièges."),

# ───────────────────────────── SÉNAT ─────────────────────────────
("chapter", "Le Sénat"),

("section", "Rôle et composition (article 20)"),
("ul", [
 "Le Sénat **représente les collectivités territoriales décentralisées**.",
 "**Chaque région est représentée par dix sénateurs** : **sept élus** au suffrage universel "
 "indirect sur une base régionale et **trois nommés** par le Président de la République.",
 "Le Cameroun comptant **dix régions**, le Sénat compte **100 sénateurs**, dont **70 élus** et "
 "**30 nommés**.",
 "Les candidats et les personnalités nommées doivent avoir **quarante ans révolus** à la date de "
 "l'élection ou de la nomination.",
 "Le mandat des sénateurs est de **cinq ans**.",
]),
("p", "Le Sénat a été installé en 2013, dix-sept ans après avoir été prévu par la révision de "
      "1996 : c'est pourquoi d'anciennes fiches présentent encore un Parlement monocaméral. "
      "Le collège électoral des sénateurs élus est composé des conseillers régionaux et des "
      "conseillers municipaux ; avant la mise en place des régions, il était composé exclusivement "
      "de conseillers municipaux (disposition transitoire de l'article 67). [S6] [S7]"),

("section", "Élection et statut des sénateurs"),
("p", "Chaque région constitue une circonscription sénatoriale. Les sénateurs élus le sont au "
      "scrutin de liste, sans vote préférentiel ni panachage, selon le mécanisme mixte "
      "majoritaire et proportionnel du Code électoral. Les listes doivent tenir compte des "
      "composantes sociologiques de la région et du genre. Parmi les conditions de candidature "
      "figurent la nationalité camerounaise et le rattachement effectif à la région concernée. [S6] [S7]"),

("section", "Organisation et fonctionnement"),
("ul", [
 "**Sessions** : trois sessions ordinaires de trente jours au maximum par an, en mars, juin et "
 "novembre ; sessions extraordinaires de quinze jours au maximum, sur ordre du jour déterminé, "
 "à la demande du Président de la République ou d'un tiers des sénateurs (art. 21).",
 "**Séances** : publiques, avec huis clos exceptionnel à la demande du Gouvernement ou de la "
 "majorité absolue des membres (art. 22).",
 "**Bureau** : la présentation officielle du Sénat fait état d'un Président, d'un premier "
 "Vice-Président, de quatre Vice-Présidents, de Questeurs et de Secrétaires, assistés d'un "
 "Secrétaire général ; les membres du bureau sont élus pour un an et rééligibles. [S7]",
 "**Commissions générales** : le Sénat organise neuf commissions générales dont les domaines "
 "recoupent ceux de l'Assemblée nationale (lois constitutionnelles et justice ; finances et "
 "budget ; affaires étrangères ; défense et sécurité ; affaires économiques et aménagement du "
 "territoire ; éducation et jeunesse ; affaires culturelles, sociales et familiales ; production "
 "et échanges ; résolutions et pétitions). [S7]",
]),

("section", "Compétences (article 24)"),
("ul", [
 "Le Sénat **adopte les lois à la majorité simple** des sénateurs.",
 "Il peut **amender** un texte : les amendements sont retenus s'ils sont approuvés à la majorité "
 "simple des sénateurs.",
 "Il peut **rejeter tout ou partie** d'un texte : le rejet doit être approuvé à la **majorité "
 "absolue** des sénateurs.",
 "En cas de seconde lecture demandée par le Président de la République, les lois sont adoptées "
 "à la **majorité absolue** des sénateurs.",
 "Il participe au **contrôle de l'action du Gouvernement** (questions, commissions d'enquête) et "
 "à la **mise en accusation** du Président devant la Haute Cour de justice.",
]),

("box", "warn", "Ce que le Sénat ne fait pas",
 "Le Sénat **ne peut pas renverser le Gouvernement** : la question de confiance et la motion de "
 "censure se jouent devant la **seule Assemblée nationale** (art. 34). Le bicamérisme camerounais "
 "est donc **inégalitaire** : en cas de désaccord persistant, c'est l'Assemblée nationale qui "
 "peut statuer définitivement."),

("subsection", "Repère d'actualité (donnée datée)"),
("p", "Le 17 mars 2026, le Sénat a élu **Sa Majesté Aboubakary ABDOULAYE**, lamido de Rey-Bouba, "
      "à sa présidence, en remplacement de Marcel Niat Njifenji, président du Sénat depuis 2013. [S10] "
      "La fonction conserve une portée constitutionnelle majeure : le Président du Sénat assure "
      "l'intérim de la Présidence de la République dans le scénario de l'article 6 révisé où le "
      "poste de Vice-Président n'est pas pourvu ou son titulaire empêché."),

# ───────────────────────────── PROCÉDURE LÉGISLATIVE ─────────────────────────────
("chapter", "La procédure législative et les rapports exécutif–Parlement"),

("section", "L'initiative des lois (articles 25 et 29)"),
("p", "L'initiative des lois appartient **concurremment au Président de la République et aux "
      "membres du Parlement**. Un texte déposé par le Président est un **projet de loi** ; un "
      "texte déposé par un parlementaire est une **proposition de loi**. Les projets et "
      "propositions sont déposés **à la fois** sur le bureau de l'Assemblée nationale et sur "
      "celui du Sénat, et sont examinés par les commissions compétentes avant la discussion en "
      "séance plénière. Ils peuvent faire l'objet d'amendements."),

("section", "Le domaine de la loi (article 26)"),
("p", "La loi est votée par le Parlement. Relèvent notamment du domaine de la loi :"),
("ul", [
 "**Les droits, garanties et obligations fondamentaux du citoyen** : sauvegarde de la liberté et "
 "de la sécurité individuelles ; régime des libertés publiques ; droit du travail, droit "
 "syndical et protection sociale ; devoirs du citoyen au regard de la défense nationale.",
 "**Le statut des personnes et le régime des biens** : nationalité, état et capacité des "
 "personnes, régimes matrimoniaux, successions et libéralités ; obligations civiles et "
 "commerciales ; propriété mobilière et immobilière.",
 "**L'organisation politique, administrative et judiciaire** : régime des élections "
 "présidentielle, législatives, sénatoriales, régionales et locales et des référendums ; régime "
 "des associations et des partis politiques ; organisation des collectivités territoriales "
 "décentralisées ; règles générales de la défense nationale ; organisation judiciaire et "
 "création des ordres de juridiction ; **détermination des crimes et délits, institution des "
 "peines, procédure pénale, procédure civile, voies d'exécution et amnistie**.",
 "**Les questions financières et patrimoniales** : émission de la monnaie ; budget ; création "
 "des impôts et taxes, assiette, taux et recouvrement ; régime domanial, foncier et minier ; "
 "régime des ressources naturelles.",
 "**La programmation des objectifs de l'action économique et sociale.**",
 "**Le régime de l'éducation.**",
]),
("box", "key", "Le point le plus utile pour un policier",
 "C'est la **loi**, et elle seule, qui détermine les crimes et délits, institue les peines et "
 "fixe la procédure pénale (art. 26, al. 2, c, 6). Aucun règlement ne peut créer une infraction. "
 "C'est le fondement du principe de **légalité des délits et des peines**, complété par le "
 "préambule : nul ne peut être poursuivi, arrêté ou détenu que dans les cas et selon les formes "
 "déterminés par la loi, et la loi n'a pas d'effet rétroactif."),

("section", "Pouvoir réglementaire et ordonnances (articles 27 et 28)"),
("p", "Les matières autres que celles du domaine de la loi **ressortissent au pouvoir "
      "réglementaire** (art. 27). Dans les matières de l'article 26, le Parlement peut **habiliter "
      "le Président de la République, pendant un délai limité et sur des objets déterminés, à "
      "prendre des ordonnances**. Ces ordonnances entrent en vigueur **dès leur publication** ; "
      "elles sont déposées sur les bureaux des deux chambres aux fins de ratification dans le "
      "délai fixé par la loi d'habilitation ; elles conservent un **caractère réglementaire tant "
      "qu'elles ne sont pas ratifiées** et demeurent en vigueur tant que le Parlement n'a pas "
      "refusé de les ratifier."),

("section", "La navette entre les deux chambres (article 30)"),
("ol", [
 "Le texte adopté par l'Assemblée nationale est **aussitôt transmis** au Président du Sénat par "
 "le Président de l'Assemblée nationale.",
 "Le Président du Sénat le soumet à la délibération du Sénat, qui dispose de **dix jours** à "
 "compter de la réception, ou de **cinq jours** pour les textes dont le Gouvernement a déclaré "
 "l'urgence.",
 "**Si le Sénat adopte le texte** : il est retourné au Président de l'Assemblée nationale, qui "
 "le transmet dans les **quarante-huit heures** au Président de la République aux fins de "
 "promulgation.",
 "**Si le Sénat amende le texte** (amendements approuvés à la majorité simple des sénateurs) : "
 "le texte amendé retourne à l'Assemblée nationale, qui adopte ou rejette les amendements à la "
 "majorité simple des députés ; le texte définitif est transmis au Président de la République.",
 "**Si le Sénat rejette tout ou partie du texte** (rejet approuvé à la majorité absolue des "
 "sénateurs) : le texte, accompagné de l'exposé des motifs du rejet, retourne à l'Assemblée "
 "nationale, qui peut l'adopter à la **majorité absolue** des députés ; il est alors transmis "
 "pour promulgation.",
 "**En l'absence de cette majorité absolue** : le Président de la République peut provoquer la "
 "réunion d'une **commission mixte paritaire** chargée de proposer un texte commun. Ce texte est "
 "soumis pour approbation aux deux chambres, aucun amendement n'étant recevable sauf accord du "
 "Président. En cas d'échec de la commission ou de non-adoption, le Président peut soit demander "
 "à l'**Assemblée nationale de statuer définitivement**, soit **déclarer le texte caduc**.",
]),

("section", "Promulgation et publication (article 31)"),
("ul", [
 "Le Président de la République promulgue les lois **dans un délai de quinze jours** à compter "
 "de leur transmission, s'il ne demande pas de seconde lecture et ne saisit pas le Conseil "
 "constitutionnel.",
 "À l'issue de ce délai, **après avoir constaté sa carence**, le **Président de l'Assemblée "
 "nationale peut se substituer** au Président de la République pour promulguer.",
 "La publication est effectuée au **Journal officiel** de la République, **en français et en "
 "anglais**.",
 "La **saisine du Conseil constitutionnel suspend** le délai de promulgation (art. 47, al. 3).",
]),

("box", "def", "Quatre mots à ne pas confondre",
 "**Adoption** : vote du texte par le Parlement.\n"
 "**Promulgation** : acte du Président qui atteste l'existence de la loi et ordonne son exécution.\n"
 "**Publication** : insertion au Journal officiel, qui rend la loi opposable.\n"
 "**Entrée en vigueur** : moment où la loi devient applicable, selon ce qu'elle prévoit."),

("section", "Messages et présence du Gouvernement (articles 32 et 33)"),
("p", "Le Président de la République peut, sur sa demande, être entendu par l'Assemblée "
      "nationale, par le Sénat ou par les deux chambres réunies en Congrès ; il peut également "
      "leur adresser des messages. **Ces communications ne donnent lieu à aucun débat en sa "
      "présence.** Le Premier ministre et les autres membres du Gouvernement ont accès au "
      "Parlement et peuvent participer aux débats."),

("section", "La responsabilité du Gouvernement (article 34)"),
("subsection", "La question de confiance"),
("p", "Lors de la session au cours de laquelle le projet de loi de finances est examiné, le "
      "Premier ministre présente à l'Assemblée nationale le programme économique, financier, "
      "social et culturel du Gouvernement. Après délibération du conseil ministériel, il peut "
      "**engager la responsabilité du Gouvernement** devant l'Assemblée nationale sur un "
      "programme ou sur une déclaration de politique générale. Le vote ne peut intervenir **moins "
      "de quarante-huit heures** après la question de confiance. La confiance est refusée à la "
      "**majorité absolue des membres** de l'Assemblée ; **seuls les votes défavorables sont "
      "recensés**."),
("subsection", "La motion de censure"),
("ul", [
 "Elle doit être **signée par au moins un tiers** des membres de l'Assemblée nationale pour être "
 "recevable.",
 "Le vote ne peut intervenir **moins de quarante-huit heures** après le dépôt.",
 "Elle est adoptée à la **majorité des deux tiers des membres composant** l'Assemblée nationale ; "
 "**seuls les votes favorables sont recensés**.",
 "En cas de rejet, les signataires ne peuvent en déposer une nouvelle **avant un délai d'un an**, "
 "sauf dans le cas de l'engagement de responsabilité sur un texte.",
]),
("subsection", "L'engagement de responsabilité sur un texte"),
("p", "Après délibération du conseil ministériel, le Premier ministre peut engager la "
      "responsabilité du Gouvernement sur le **vote d'un texte**. Le texte est alors considéré "
      "comme adopté, **sauf si une motion de censure déposée dans les vingt-quatre heures** qui "
      "suivent est votée dans les conditions ci-dessus."),
("subsection", "Les suites"),
("p", "Lorsque l'Assemblée nationale adopte une motion de censure ou refuse la confiance, le "
      "Premier ministre **doit remettre au Président de la République la démission du "
      "Gouvernement**. Le Président peut **reconduire le Premier ministre** dans ses fonctions et "
      "lui demander de former un nouveau Gouvernement."),

("table",
 ["Mécanisme", "Initiative", "Majorité requise", "Votes recensés"],
 [
  ["Question de confiance", "Premier ministre, après délibération du conseil ministériel", "Confiance refusée à la majorité absolue des membres", "Seuls les votes défavorables"],
  ["Motion de censure", "Au moins un tiers des députés", "Deux tiers des membres composant l'Assemblée", "Seuls les votes favorables"],
  ["Engagement sur un texte", "Premier ministre", "Texte adopté sauf censure votée dans les mêmes conditions", "Censure déposée dans les 24 heures"],
 ],
 [0.22, 0.28, 0.30, 0.20]),

("section", "Le contrôle parlementaire (article 35)"),
("ul", [
 "Le Parlement contrôle l'action gouvernementale par les **questions orales ou écrites** et par "
 "la constitution de **commissions d'enquête** sur des objets déterminés.",
 "Le Gouvernement **fournit des renseignements** au Parlement, sous réserve des impératifs de la "
 "défense nationale, de la sécurité de l'État ou du **secret de l'information judiciaire**.",
 "Au cours de chaque session ordinaire, **une séance par semaine** est réservée par priorité aux "
 "questions des parlementaires et aux réponses du Gouvernement.",
]),

("section", "Le référendum (article 36)"),
("p", "Après consultation du Président du Conseil constitutionnel, du Président de l'Assemblée "
      "nationale et du Président du Sénat, le Président de la République peut soumettre au "
      "référendum tout projet de réforme qui, bien que relevant du domaine de la loi, serait "
      "susceptible d'avoir des répercussions profondes sur l'avenir de la Nation et les "
      "institutions : projets portant sur l'organisation des pouvoirs publics ou sur la révision "
      "de la Constitution, ratification de traités d'importance particulière, certaines réformes "
      "du statut des personnes et du régime des biens. Le projet est **adopté à la majorité des "
      "suffrages exprimés**."),

("section", "Le Conseil constitutionnel (articles 46 à 52)"),
("ul", [
 "Il est l'**instance compétente en matière constitutionnelle** et l'**organe régulateur du "
 "fonctionnement des institutions**.",
 "Il statue souverainement sur la **constitutionnalité des lois, des traités et accords "
 "internationaux**, sur les **règlements intérieurs** des deux chambres avant leur mise en "
 "application, et sur les **conflits d'attribution** entre institutions de l'État, entre l'État "
 "et les régions, ou entre régions.",
 "Il est saisi par le **Président de la République**, le **Président de l'Assemblée nationale**, "
 "le **Président du Sénat**, **un tiers des députés** ou **un tiers des sénateurs** ; les "
 "présidents des exécutifs régionaux peuvent le saisir lorsque les intérêts de leur région sont "
 "en cause.",
 "Il **veille à la régularité de l'élection présidentielle, des élections parlementaires et des "
 "consultations référendaires** et en **proclame les résultats** (art. 48).",
 "Il statue dans un **délai de quinze jours**, ramené à **huit jours** à la demande du Président "
 "de la République (art. 49).",
 "Ses **décisions ne sont susceptibles d'aucun recours** et s'imposent aux pouvoirs publics et à "
 "toutes les autorités administratives, militaires et juridictionnelles ainsi qu'à toute "
 "personne (art. 50).",
 "Il comprend **onze membres** nommés par le Président de la République pour un mandat de **six "
 "ans éventuellement renouvelable** (durée issue de la révision de 2008) : trois désignés par le "
 "Président de la République dont le président du Conseil, trois par le Président de l'Assemblée "
 "nationale après avis du bureau, trois par le Président du Sénat après avis du bureau, et deux "
 "par le Conseil supérieur de la magistrature. Les anciens Présidents de la République en sont "
 "membres **de droit et à vie** (art. 51).",
]),

("section", "Les traités (articles 43 à 45)"),
("p", "Le Président de la République **négocie et ratifie** les traités et accords "
      "internationaux. Ceux qui concernent le domaine de la loi défini à l'article 26 sont soumis, "
      "**avant ratification, à l'approbation en forme législative par le Parlement**. Si le "
      "Conseil constitutionnel déclare qu'un traité comporte une clause contraire à la "
      "Constitution, l'approbation ou la ratification ne peut intervenir qu'après révision de la "
      "Constitution. Les traités régulièrement approuvés ou ratifiés ont, dès leur publication, "
      "une **autorité supérieure à celle des lois**, sous réserve de réciprocité."),

("section", "La révision de la Constitution (articles 63 et 64)"),
("ul", [
 "L'initiative appartient **concurremment au Président de la République et au Parlement**.",
 "Toute proposition émanant des parlementaires doit être signée par **un tiers au moins** des "
 "membres de l'une ou l'autre chambre.",
 "Le Parlement se réunit en **Congrès** ; le texte est adopté à la **majorité absolue des "
 "membres le composant**.",
 "Le Président peut demander une **seconde lecture** : la révision est alors votée à la "
 "**majorité des deux tiers** des membres composant le Parlement.",
 "Le Président peut soumettre la révision au **référendum** : le texte est alors adopté à la "
 "**majorité simple des suffrages exprimés**.",
 "**Limite absolue** : aucune révision ne peut porter atteinte à la **forme républicaine**, à "
 "l'**unité et à l'intégrité territoriale** de l'État, ni aux **principes démocratiques** qui "
 "régissent la République (art. 64).",
]),
("p", "C'est par cette procédure qu'a été adoptée la révision du 4 avril 2026, votée en Congrès "
      "puis promulguée le 14 avril 2026. [S3]"),

# ───────────────────────────── SYNTHÈSES ─────────────────────────────
("chapter", "Tableaux de synthèse et méthode"),

("section", "Qui fait quoi ?"),
("table",
 ["Institution", "Fonction principale", "Base constitutionnelle"],
 [
  ["Président de la République", "Chef de l'État ; définit la politique de la Nation ; arbitre ; nomme ; promulgue ; pouvoirs de crise", "Art. 5 à 10"],
  ["Vice-Président", "Assiste le Président par délégation expresse ; achève le mandat en cas de vacance", "Art. 5, 6, 7 et 10 (révision 2026)"],
  ["Gouvernement", "Met en œuvre la politique définie par le Président ; responsable devant l'Assemblée nationale", "Art. 11"],
  ["Premier ministre", "Chef du Gouvernement ; exécute les lois ; pouvoir réglementaire subordonné", "Art. 12"],
  ["Assemblée nationale", "Vote la loi et le budget ; contrôle ; première chambre de la navette", "Art. 15 à 19, 30 à 35"],
  ["Sénat", "Représente les collectivités territoriales ; seconde chambre de la navette ; contrôle", "Art. 20 à 24, 30 à 35"],
  ["Congrès", "Message présidentiel, serment des membres du Conseil constitutionnel, révision", "Art. 14 et 63"],
  ["Conseil constitutionnel", "Constitutionnalité, régulation, proclamation des résultats", "Art. 46 à 52"],
 ],
 [0.24, 0.52, 0.24]),

("section", "Assemblée nationale et Sénat : les différences"),
("table",
 ["Critère", "Assemblée nationale", "Sénat"],
 [
  ["Représentation", "La Nation tout entière", "Les collectivités territoriales décentralisées"],
  ["Effectif constitutionnel", "180 députés", "100 sénateurs"],
  ["Désignation", "Suffrage universel direct et secret", "70 élus au suffrage indirect + 30 nommés par le Président"],
  ["Base territoriale", "Circonscriptions fixées par la loi", "Dix sénateurs par région"],
  ["Durée du mandat", "Cinq ans", "Cinq ans"],
  ["Âge minimal", "23 ans (Code électoral)", "40 ans (Constitution, art. 20)"],
  ["Sessions", "Trois sessions ordinaires de 30 jours ; extraordinaire 15 jours", "Même régime"],
  ["Dissolution possible", "Oui, par le Président (art. 8, al. 12)", "Non prévue par la Constitution"],
  ["Renverser le Gouvernement", "Oui (question de confiance, motion de censure)", "Non"],
  ["Dernier mot dans la navette", "Oui, si le Président le demande (art. 30)", "Non"],
  ["Présidence au " + DATE_MAJ, "Théodore Datouo (depuis le 17 mars 2026)", "Aboubakary Abdoulaye (depuis le 17 mars 2026)"],
 ],
 [0.24, 0.38, 0.38]),

("section", "Les délais et chiffres à retenir"),
("table",
 ["Chiffre", "Ce qu'il désigne"],
 [
  ["20 ans", "Âge de participation au vote (art. 2, al. 3)"],
  ["23 ans", "Âge minimal du candidat à la députation (Code électoral)"],
  ["35 ans", "Âge minimal du candidat à la Présidence (art. 6)"],
  ["40 ans", "Âge minimal du sénateur (art. 20)"],
  ["5 ans", "Mandat des députés et des sénateurs"],
  ["7 ans", "Mandat du Président de la République"],
  ["6 ans", "Mandat des membres du Conseil constitutionnel (depuis 2008)"],
  ["180 / 100", "Députés / sénateurs"],
  ["70 / 30", "Sénateurs élus / sénateurs nommés"],
  ["3 × 30 jours", "Sessions ordinaires annuelles et durée maximale de chacune"],
  ["15 jours", "Durée maximale d'une session extraordinaire ; délai de promulgation ; délai de décision du Conseil constitutionnel"],
  ["10 / 5 jours", "Délai d'examen du Sénat dans la navette (procédure normale / urgence)"],
  ["48 heures", "Délai avant le vote d'une question de confiance ou d'une motion de censure ; transmission du texte adopté pour promulgation"],
  ["24 heures", "Délai de dépôt d'une motion de censure après un engagement de responsabilité sur un texte"],
  ["20 à 50 jours", "Fenêtre de l'élection présidentielle avant l'expiration du mandat en cours"],
  ["20 à 120 jours", "Fenêtre du scrutin en cas de vacance sans Vice-Président en fonctions"],
  ["1/3 – 2/3 – 4/5", "Dépôt d'une motion de censure ; adoption de la censure et seconde lecture d'une révision ; mise en accusation du Président"],
 ],
 [0.22, 0.78]),

("section", "Méthode pour une question de cours"),
("ol", [
 "**Définir** le sujet en une phrase juridique.",
 "**Annoncer le fondement** : citer l'article (5, 6, 8, 14, 15, 20, 26, 30, 31, 34, 35…).",
 "**Classer** : statut, composition, compétences, fonctionnement, limites.",
 "**Distinguer** la règle et l'actualité : un titulaire change, un article demeure.",
 "**Conclure** par la portée pratique, en particulier pour la police : légalité, ordre public, "
 "responsabilité, libertés.",
]),

("box", "method", "Modèle de réponse courte",
 "**Question : « Quel est le rôle du Parlement camerounais ? »**\n"
 "« Selon l'article 14 de la Constitution, le pouvoir législatif est exercé par un Parlement "
 "bicaméral composé de l'Assemblée nationale et du Sénat. Le Parlement légifère et contrôle "
 "l'action du Gouvernement. Il vote la loi selon la procédure de navette de l'article 30, vote "
 "le budget de l'État, contrôle le Gouvernement par les questions et les commissions d'enquête "
 "de l'article 35, et peut mettre en cause sa responsabilité dans les conditions de l'article 34, "
 "cette dernière prérogative appartenant à la seule Assemblée nationale. »"),

# ───────────────────────────── ENTRAÎNEMENT ─────────────────────────────
("chapter", "Entraînement : QCM et corrigé commenté"),

("section", "QCM (une seule réponse exacte par question)"),
("qcm", [
 ("Le Parlement camerounais comprend :",
  ["le Gouvernement et le Conseil constitutionnel",
   "l'Assemblée nationale et le Sénat",
   "l'Assemblée nationale et la Cour suprême"]),
 ("Le Président de la République est élu pour :", ["cinq ans", "six ans", "sept ans"]),
 ("Depuis la révision de 2008, le Président de la République est :",
  ["rééligible sans limitation", "limité à deux mandats", "élu par le Parlement"]),
 ("Le Président de la République est élu au :",
  ["suffrage universel indirect", "suffrage universel direct, égal et secret", "scrutin public du Congrès"]),
 ("Le Chef du Gouvernement est :",
  ["le Président de la République", "le Président de l'Assemblée nationale", "le Premier ministre"]),
 ("Le nombre constitutionnel de députés est :", ["100", "180", "360"]),
 ("Le Sénat compte :", ["70 membres", "100 membres", "180 membres"]),
 ("Chaque région est représentée au Sénat par :", ["7 sénateurs", "10 sénateurs", "30 sénateurs"]),
 ("Les trente sénateurs nommés le sont par :",
  ["le Conseil constitutionnel", "le Président de la République", "les maires"]),
 ("Les sessions ordinaires du Parlement se tiennent en :",
  ["janvier, mai et septembre", "mars, juin et novembre", "février, juillet et décembre"]),
 ("La durée maximale d'une session extraordinaire est de :", ["7 jours", "15 jours", "30 jours"]),
 ("L'âge minimal pour être sénateur est de :", ["35 ans", "40 ans", "45 ans"]),
 ("L'initiative des lois appartient :",
  ["au seul Gouvernement", "au Président de la République et aux membres du Parlement", "au Conseil constitutionnel"]),
 ("Un texte déposé par un parlementaire s'appelle :",
  ["un projet de loi", "une proposition de loi", "une ordonnance"]),
 ("Dans la navette, le délai ordinaire d'examen du Sénat est de :", ["5 jours", "10 jours", "45 jours"]),
 ("Le délai de promulgation de l'article 31 est de :", ["15 jours", "30 jours", "120 jours"]),
 ("Une motion de censure doit être signée par au moins :",
  ["un dixième des députés", "un tiers des députés", "les deux tiers des sénateurs"]),
 ("La motion de censure est adoptée à la majorité :",
  ["simple des votants", "absolue des députés", "des deux tiers des membres composant l'Assemblée nationale"]),
 ("Depuis la révision de 2026, en cas de vacance de la Présidence :",
  ["le Président du Sénat achève toujours le mandat",
   "le Vice-Président achève le mandat, et à défaut le Président du Sénat assure l'intérim avant un nouveau scrutin",
   "le Premier ministre devient Président"]),
 ("Les deux chambres réunies forment :",
  ["le Congrès", "le Conseil des ministres", "la Haute Cour de justice"]),
 ("La mise en accusation du Président devant la Haute Cour de justice exige :",
  ["la majorité simple des deux chambres",
   "un vote identique des deux chambres à la majorité des quatre cinquièmes",
   "une décision du Conseil constitutionnel"]),
 ("L'état d'exception est proclamé :",
  ["par une loi du Parlement", "par décret du Président de la République", "par arrêté du Premier ministre"]),
 ("Le droit de grâce est exercé par le Président :",
  ["après avis du Conseil supérieur de la magistrature", "après vote du Parlement", "librement et sans avis"]),
 ("La détermination des crimes et délits relève :",
  ["du pouvoir réglementaire", "du domaine de la loi", "d'une décision du Conseil constitutionnel"]),
 ("Le Conseil constitutionnel statue normalement dans un délai de :",
  ["8 jours", "15 jours", "30 jours"]),
]),

("section", "Corrigé commenté"),
("table",
 ["Q", "Réponse et justification"],
 [
  ["1", "**B.** Article 14, alinéa 1 : Assemblée nationale et Sénat."],
  ["2", "**C.** Article 6, alinéa 2 : sept ans."],
  ["3", "**A.** La loi n° 2008/001 a supprimé « renouvelable une fois » ; le texte dit « Il est rééligible »."],
  ["4", "**B.** Article 6, alinéa 1 : suffrage universel direct, égal et secret, à la majorité des suffrages exprimés."],
  ["5", "**C.** Article 12, alinéa 1 : le Premier ministre est le Chef du Gouvernement."],
  ["6", "**B.** Article 15 : 180 députés ; ce nombre peut être modifié par la loi."],
  ["7", "**B.** Article 20 : dix régions × dix sénateurs = 100."],
  ["8", "**B.** Article 20, alinéa 2 : dix sénateurs par région, dont 7 élus et 3 nommés."],
  ["9", "**B.** Les trois sénateurs par région non élus sont nommés par le Président de la République."],
  ["10", "**B.** Article 14, alinéa 3, a, tel que modifié en 2008 : mars, juin et novembre."],
  ["11", "**B.** Articles 16 et 21 : quinze jours au maximum, sur ordre du jour déterminé."],
  ["12", "**B.** Article 20, alinéa 3 : quarante ans révolus à la date de l'élection ou de la nomination."],
  ["13", "**B.** Article 25 : initiative concurrente du Président de la République et des membres du Parlement."],
  ["14", "**B.** Le texte d'origine parlementaire est une proposition de loi ; celui du Président, un projet de loi."],
  ["15", "**B.** Article 30, alinéa 3 : dix jours, ramenés à cinq jours en cas d'urgence déclarée par le Gouvernement."],
  ["16", "**A.** Article 31, alinéa 1 : quinze jours, sauf seconde lecture ou saisine du Conseil constitutionnel."],
  ["17", "**B.** Article 34, alinéa 3 : au moins un tiers des membres de l'Assemblée nationale."],
  ["18", "**C.** Article 34, alinéa 3 : deux tiers des membres composant l'Assemblée ; seuls les votes favorables sont recensés."],
  ["19", "**B.** Article 6 révisé en 2026 : le Vice-Président achève le mandat ; si le poste n'est pas pourvu ou si son titulaire est empêché, scrutin dans 20 à 120 jours avec intérim du Président du Sénat."],
  ["20", "**A.** Article 14, alinéa 4 : les deux chambres réunies en Congrès."],
  ["21", "**B.** Article 53, alinéa 2 : vote identique des deux chambres, au scrutin public, à la majorité des quatre cinquièmes."],
  ["22", "**B.** Article 9, alinéa 2 : proclamation par décret du Président de la République."],
  ["23", "**A.** Article 8, alinéa 7 : après avis du Conseil supérieur de la magistrature."],
  ["24", "**B.** Article 26, alinéa 2, c, 6 : domaine de la loi."],
  ["25", "**B.** Article 49 : quinze jours, ramenés à huit à la demande du Président de la République."],
 ],
 [0.06, 0.94]),

("section", "Sujets de rédaction possibles"),
("ol", [
 "Le Président de la République : statut, élection et attributions.",
 "Le bicamérisme camerounais : unité de fonction, inégalité de pouvoirs.",
 "Comparez l'Assemblée nationale et le Sénat.",
 "La procédure d'adoption d'une loi au Cameroun, du dépôt à la publication.",
 "Le contrôle de l'action gouvernementale par le Parlement.",
 "La vacance de la Présidence de la République après la révision de 2026.",
 "Les pouvoirs de crise du Président de la République et les garanties des libertés.",
 "Le rôle du Conseil constitutionnel dans l'équilibre des institutions.",
]),

# ───────────────────────────── ANNEXES ─────────────────────────────
("chapter", "Annexes"),

("section", "Les articles à relire en priorité"),
("table",
 ["Articles", "Contenu"],
 [
  ["1 à 4", "Nature de l'État, souveraineté, partis politiques, autorités de l'État"],
  ["5 à 10", "Président de la République : statut, élection, serment, attributions, crises, nominations, Vice-Président"],
  ["11 à 13", "Gouvernement, Premier ministre, incompatibilités"],
  ["14", "Parlement : composition, missions, sessions, Congrès"],
  ["15 à 19", "Assemblée nationale"],
  ["20 à 24", "Sénat"],
  ["25 à 31", "Initiative, domaine de la loi, ordonnances, navette, promulgation"],
  ["32 à 36", "Messages, accès du Gouvernement, confiance et censure, contrôle, référendum"],
  ["37 à 42", "Pouvoir judiciaire et Cour suprême"],
  ["43 à 45", "Traités et accords internationaux"],
  ["46 à 52", "Conseil constitutionnel"],
  ["53", "Haute Cour de justice et mise en accusation"],
  ["55 à 62", "Collectivités territoriales décentralisées et régions"],
  ["63 à 66", "Révision, préambule, déclaration des biens"],
 ],
 [0.16, 0.84]),

("section", "Chronologie institutionnelle"),
("table",
 ["Date", "Repère"],
 [
  ["1er janvier 1960", "Indépendance du Cameroun"],
  ["2 juin 1972", "Constitution de l'État unitaire"],
  ["4 février 1984", "La République unie du Cameroun devient la République du Cameroun ; suppression de la vice-présidence héritée des textes antérieurs"],
  ["18 janvier 1996", "Loi n° 96/06 : révision générale ; décentralisation, Sénat, Conseil constitutionnel prévus"],
  ["19 avril 2012", "Loi n° 2012/001 portant Code électoral"],
  ["14 avril 2008", "Loi n° 2008/001 : le Président devient rééligible ; sessions ordinaires en mars, juin et novembre ; ajustements sur la vacance, le Conseil constitutionnel et la Haute Cour"],
  ["2013", "Installation effective du Sénat (70 élus, 30 nommés)"],
  ["4 avril 2026", "Le Parlement réuni en Congrès adopte la révision créant le poste de Vice-Président"],
  ["14 avril 2026", "Promulgation de la révision constitutionnelle de 2026"],
  ["17 mars 2026", "Théodore Datouo élu Président de l'Assemblée nationale ; Aboubakary Abdoulaye élu Président du Sénat"],
  [DATE_MAJ, "Date d'arrêt des données de ce document"],
 ],
 [0.20, 0.80]),

("section", "Glossaire"),
("dl", [
 ("Amendement", "Modification proposée à un texte en cours d'examen."),
 ("Amnistie", "Mesure législative qui efface l'infraction elle-même ; à distinguer de la grâce."),
 ("Bicamérisme", "Organisation du Parlement en deux chambres."),
 ("Caducité", "Perte d'effet d'un texte, que le Président peut déclarer en cas d'échec de la navette."),
 ("Congrès", "Réunion de l'Assemblée nationale et du Sénat dans les cas prévus par l'article 14."),
 ("Commission mixte paritaire", "Commission réunissant députés et sénateurs pour proposer un texte commun."),
 ("Décret", "Acte réglementaire du Président de la République ou du Premier ministre."),
 ("Grâce", "Dispense totale ou partielle d'exécution d'une peine, accordée par le Président."),
 ("Immunité", "Protection juridique attachée à une fonction ; elle n'est pas une impunité."),
 ("Majorité absolue", "Plus de la moitié des membres composant l'organe."),
 ("Majorité simple", "Majorité des suffrages exprimés lors du vote."),
 ("Mandat impératif", "Instruction contraignante donnée à un élu ; il est nul en droit camerounais."),
 ("Navette", "Circulation d'un texte entre l'Assemblée nationale et le Sénat."),
 ("Ordonnance", "Acte pris par le Président dans une matière législative, sur habilitation du Parlement."),
 ("Promulgation", "Acte par lequel le Président atteste l'existence de la loi et en ordonne l'exécution."),
 ("Questeur", "Membre du bureau chargé des services administratifs et financiers de la chambre."),
 ("Rééligible", "Qui peut être élu à nouveau, sans limitation du nombre de mandats."),
 ("Suffrages exprimés", "Votes valablement émis, hors bulletins nuls et blancs."),
 ("Vacance", "Situation dans laquelle la Présidence est privée de titulaire par décès, démission ou empêchement définitif."),
]),
]
