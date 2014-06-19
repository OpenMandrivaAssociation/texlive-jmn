# revision 22719
# category Package
# catalog-ctan undef
# catalog-date undef
# catalog-license undef
# catalog-version undef
Name:		texlive-jmn
Version:	20140619
Release:	1
Summary:	TeXLive jmn package
Group:		Publishing
URL:		http://tug.org/texlive
License:	http://www.tug.org/texlive/LICENSE.TL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/jmn.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
TeXLive jmn package.

%post
    %{_sbindir}/texlive.post

%postun
    if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/fonts/afm/jmn/hans/hans-sh.afm
%{_texmfdistdir}/fonts/afm/jmn/hans/hans.afm
%{_texmfdistdir}/fonts/enc/dvips/jmn/hans.enc
%{_texmfdistdir}/fonts/map/dvips/jmn/hans.map
%{_texmfdistdir}/fonts/tfm/jmn/hans/hans-sh.tfm
%{_texmfdistdir}/fonts/tfm/jmn/hans/hans.tfm
%{_texmfdistdir}/fonts/type1/jmn/hans/hans-sh.pfb
%{_texmfdistdir}/fonts/type1/jmn/hans/hans-sh.pfm
%{_texmfdistdir}/fonts/type1/jmn/hans/hans.pfb
%{_texmfdistdir}/fonts/type1/jmn/hans/hans.pfm

#-----------------------------------------------------------------------
%prep
%setup -c -a0

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar fonts %{buildroot}%{_texmfdistdir}
