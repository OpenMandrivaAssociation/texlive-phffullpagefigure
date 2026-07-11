%global tl_name phffullpagefigure
%global tl_revision 41857

Name:		texlive-%{tl_name}
Epoch:		1
Version:	1.0
Release:	%{tl_revision}.1
Summary:	Figures which fill up a whole page
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/phffullpagefigure
License:	lppl1.3
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/phffullpagefigure.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/phffullpagefigure.doc.r%{tl_revision}.tar.xz
Source2:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/phffullpagefigure.source.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
This package defines a figure environment which provides the figure
content on its own page, with the corresponding caption reading for
example "Figure 3 (on next page): <caption>".

