%global tl_name jmn
%global tl_revision 45751

Name:		texlive-%{tl_name}
Version:	%{tl_revision}
Release:	1
Summary:	special fonts for ConTeXt
Group:		Publishing
URL:		https://www.ctan.org/pkg/jmn
License:	LPPL
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/jmn.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
special fonts for ConTeXt

