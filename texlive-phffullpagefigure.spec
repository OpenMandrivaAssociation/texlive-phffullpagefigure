Name:		texlive-phffullpagefigure
Version:	41857
Release:	1
Summary:	Figures which fill up a whole page
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/phffullpagefigure
License:	lppl1.3
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/phffullpagefigure.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/phffullpagefigure.doc.r%{version}.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/phffullpagefigure.source.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
This package defines a figure environment which provides the
figure content on its own page, with the corresponding caption
reading for example "Figure 3 (on next page): <caption>".

%prep
%setup -c -a1 -a2
%autopatch -p1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_texmfdistdir}
cp -a * %{buildroot}%{_texmfdistdir}

%files
%doc %{_texmfdistdir}/source/latex/phffullpagefigure
%{_texmfdistdir}/tex/latex/phffullpagefigure
%doc %{_texmfdistdir}/doc/latex/phffullpagefigure

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post
