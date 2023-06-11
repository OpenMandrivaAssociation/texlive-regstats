Name:		texlive-regstats
Version:	66795
Release:	1
Summary:	Information about register use
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/regstats
License:	LPPL1.3
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/regstats.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/regstats.doc.r%{version}.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/regstats.source.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The package will report number of used registers (counter,
dimen, skip, muskip, box, token, input, output, math families,
languages, insertions), and will compare the number to the
maximum available number of such registers.

%post
%{_sbindir}/texlive.post

%postun
if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/regstats/regstats.sty
%doc %{_texmfdistdir}/doc/latex/regstats/README
%doc %{_texmfdistdir}/doc/latex/regstats/regstats-example.log
%doc %{_texmfdistdir}/doc/latex/regstats/regstats-example.pdf
%doc %{_texmfdistdir}/doc/latex/regstats/regstats-example.tex
%doc %{_texmfdistdir}/doc/latex/regstats/regstats.pdf
#- source
%doc %{_texmfdistdir}/source/latex/regstats/regstats.drv
%doc %{_texmfdistdir}/source/latex/regstats/regstats.dtx
%doc %{_texmfdistdir}/source/latex/regstats/regstats.ins

#-----------------------------------------------------------------------
%prep
%setup -c -a1 -a2
%autopatch -p1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}
