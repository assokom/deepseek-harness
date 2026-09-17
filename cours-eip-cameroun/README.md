# Cours EIP — Président de la République et Parlement du Cameroun

Livrables :

- `cours_eip_cameroun.pdf` : document PDF final ;
- `cours_eip_cameroun.tex` : source LaTeX complet et reproductible.

## Compilation

Le document est prévu pour **LuaLaTeX** :

```bash
lualatex -interaction=nonstopmode cours_eip_cameroun.tex
lualatex -interaction=nonstopmode cours_eip_cameroun.tex
```

La seconde passe met à jour la table des matières et la pagination. Le document utilise notamment `fontspec`, `babel`, `tcolorbox`, `booktabs`, `longtable`, `tikz` et `hyperref`, disponibles dans une distribution TeX Live ou MiKTeX complète.

## Périmètre et date

Cours en français, destiné à la préparation EIP, couvrant le Président de la République, le Vice-Président créé par la loi n° 2026/002 du 14 avril 2026, le Gouvernement, l'Assemblée nationale, le Sénat, la procédure législative, le contrôle parlementaire, les articles constitutionnels essentiels, des tableaux de synthèse et un QCM corrigé.

Les données institutionnelles variables sont datées du **17 septembre 2026** et distinguées des règles constitutionnelles. La bibliographie et les URL consultées figurent dans le document et dans ses hyperliens.
