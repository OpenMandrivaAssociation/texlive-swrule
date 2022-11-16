Name:		texlive-swrule
Version:	54267
Release:	1
Summary:	Lines thicker in the middle than at the ends
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/swrule
License:	other-free
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/swrule.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
Defines commands that create rules split into a (specified)
number of pieces, whose size varies to produce the effect of a
rule that swells in its centre.

%prep
%autosetup -p1 -c

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_texmfdistdir}
cp -a * %{buildroot}%{_texmfdistdir}

%files
%{_texmfdistdir}/tex/generic/swrule

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post
