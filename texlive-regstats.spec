# revision 25050
# category Package
# catalog-ctan /macros/latex/contrib/regstats
# catalog-date 2012-01-02 14:24:13 +0100
# catalog-license lppl1.3
# catalog-version 1.0g
Name:		texlive-regstats
Version:	1.0h
Release:	2
Summary:	Information about register use
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/regstats
License:	LPPL1.3
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/regstats.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/regstats.doc.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/regstats.source.tar.xz
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
%setup -c -a0 -a1 -a2

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}


%changelog
* Thu Jan 19 2012 Paulo Andrade <pcpa@mandriva.com.br> 1.0g-2
+ Revision: 762706
- Update to latest upstream package

* Mon Jan 09 2012 Paulo Andrade <pcpa@mandriva.com.br> 1.0g-1
+ Revision: 759033
- Update to latest upstream release

* Wed Jan 04 2012 Paulo Andrade <pcpa@mandriva.com.br> 1.0f-2
+ Revision: 755657
- Rebuild to reduce used resources

* Sat Nov 05 2011 Paulo Andrade <pcpa@mandriva.com.br> 1.0f-1
+ Revision: 719447
- texlive-regstats
- texlive-regstats
- texlive-regstats
- texlive-regstats

