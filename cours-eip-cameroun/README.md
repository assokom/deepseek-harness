# Cours EIP — Le Président de la République et le Parlement au Cameroun

Support de préparation au concours d'Élève Inspecteur de Police (EIP), en français,
sur les institutions camerounaises.

## Livrables

| Fichier | Contenu |
| --- | --- |
| `cours_eip_cameroun.pdf` | Document final, 33 pages, mis en page (couverture, sommaire, encadrés, tableaux, QCM corrigé) |
| `cours_eip_cameroun.tex` | Source LaTeX autonome et compilable du même document |
| `content.py` | Source unique du contenu (texte, tableaux, QCM, sources) |
| `build.py` | Générateur : produit le `.tex` et le `.pdf` à partir de `content.py` |

## Régénérer les livrables

```bash
python3 build.py          # régénère cours_eip_cameroun.tex et cours_eip_cameroun.pdf
python3 build.py --tex    # régénère uniquement le .tex (aucune dépendance)
```

Le PDF est produit avec **ReportLab** (`pip install reportlab`), car aucune distribution
TeX n'est installable dans l'environnement de travail. Sur une machine disposant de
TeX Live ou MiKTeX, le `.tex` se compile directement :

```bash
pdflatex cours_eip_cameroun.tex
pdflatex cours_eip_cameroun.tex   # seconde passe : sommaire et pagination
```

Paquets requis par le `.tex` : `babel`, `geometry`, `lmodern`, `microtype`, `booktabs`,
`longtable`, `enumitem`, `xcolor`, `tcolorbox`, `titlesec`, `fancyhdr`, `lastpage`,
`hyperref`, `xurl`.

## Périmètre

- Cadre constitutionnel : nature de l'État, souveraineté, carte des institutions.
- Président de la République : statut (art. 5), élection et mandat (art. 6),
  serment (art. 7), attributions (art. 8), pouvoirs de crise (art. 9),
  nominations et délégations (art. 10), vacance de la Présidence, Haute Cour de justice
  (art. 53), déclaration des biens (art. 66).
- Vice-Président : fonction créée par la révision constitutionnelle adoptée le
  4 avril 2026 et promulguée le 14 avril 2026 (articles 5, 6, 7, 10, 53 et 66 modifiés).
- Gouvernement et Premier ministre (art. 11 à 13).
- Parlement : règles communes (art. 14), Assemblée nationale (art. 15 à 19),
  Sénat (art. 20 à 24).
- Procédure législative : initiative, domaine de la loi, ordonnances, navette,
  promulgation (art. 25 à 31) ; contrôle parlementaire et responsabilité du
  Gouvernement (art. 32 à 36) ; Conseil constitutionnel (art. 46 à 52) ;
  révision de la Constitution (art. 63 et 64).
- Tableaux de synthèse, chiffres et délais clés, méthode de réponse, glossaire,
  QCM de 25 questions avec corrigé commenté, sujets de rédaction.

## Fiabilité

Les règles proviennent de la Constitution du 2 juin 1972 révisée par la loi n° 96/06
du 18 janvier 1996, la loi n° 2008/001 du 14 avril 2008 et la révision de 2026, ainsi
que de la loi n° 2012/001 portant Code électoral et des documents officiels des deux
chambres. Les sources et leurs URL figurent au dernier chapitre du document.

Les données variables (titulaires de fonctions) sont **datées au 17 septembre 2026** et
signalées comme telles ; les règles constitutionnelles en sont distinguées. Aucune
nomination de Vice-Président n'est affirmée : de faux décrets ont circulé en avril 2026
et ont été démentis.
