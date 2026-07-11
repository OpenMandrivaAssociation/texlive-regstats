%global tl_name regstats
%global tl_revision 78101

Name:		texlive-%{tl_name}
Epoch:		1
Version:	1.1b
Release:	%{tl_revision}.1
Summary:	Information about register use
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/regstats
License:	lppl1.3c
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/regstats.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/regstats.doc.r%{tl_revision}.tar.xz
Source2:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/regstats.source.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
The package will report number of used registers (counter, dimen, skip,
muskip, box, token, input, output, math families, languages,
insertions), and will compare the number to the maximum available number
of such registers.

