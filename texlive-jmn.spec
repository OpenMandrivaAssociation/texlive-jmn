# revision 22719
# category Package
# catalog-ctan undef
# catalog-date undef
# catalog-license undef
# catalog-version undef
Name:		texlive-jmn
Version:	20111103
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
Conflicts:	texlive-texmf <= 20110705-3

%description
TeXLive jmn package.

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
%doc %{_tlpkgobjdir}/*.tlpobj

#-----------------------------------------------------------------------
%prep
%setup -c -a0

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar fonts %{buildroot}%{_texmfdistdir}
mkdir -p %{buildroot}%{_tlpkgobjdir}
cp -fpa tlpkg/tlpobj/*.tlpobj %{buildroot}%{_tlpkgobjdir}
