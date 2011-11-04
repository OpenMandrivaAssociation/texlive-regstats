# revision 23662
# category Package
# catalog-ctan /macros/latex/contrib/regstats
# catalog-date 2011-08-24 08:41:41 +0200
# catalog-license lppl1.3
# catalog-version 1.0f
Name:		texlive-regstats
Version:	1.0f
Release:	1
Summary:	Information about register use
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/regstats
License:	LPPL1.3
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/regstats.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/regstats.doc.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/regstats.source.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(post):	texlive-tlpkg
Conflicts:	texlive-texmf <= 20110705-3
Conflicts:	texlive-doc <= 20110705-3
Conflicts:	texlive-source <= 20110705-3

%description
The package will report number of used registers (counter,
dimen, skip, muskip, box, token, input, output, math families,
languages, insertions), and will compare the number to the
maximum available number of such registers.

%pre
    %_texmf_mktexlsr_pre

%post
    %_texmf_mktexlsr_post

%preun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_pre
    fi

%postun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_post
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
%doc %{_tlpkgobjdir}/*.tlpobj

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1 -a2

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}
mkdir -p %{buildroot}%{_tlpkgobjdir}
cp -fpa tlpkg/tlpobj/*.tlpobj %{buildroot}%{_tlpkgobjdir}
