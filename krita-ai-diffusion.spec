Name:		krita-ai-diffusion
Version:	1.20.1
Release:	1
Source0:	https://github.com/Acly/krita-ai-diffusion/releases/download/v%{version}/krita_ai_diffusion-%{version}.zip
Patch0:		krita-ai-diffusion-amd-rocm.patch
Summary:	AI image generation plugin for Krita
URL:		https://github.com/Acly/krita-ai-diffusion
License:	GPL
Group:		Graphics
BuildArch:	noarch
Requires:	(krita >= 5.2.0 with krita < 6.0.0)
Supplements:	(krita >= 5.2.0 with krita < 6.0.0)
Requires:	python-qt5-network
Requires:	python-ensurepip

%description
Generate images from within Krita with minimal fuss: Select an
area, push a button, and new content that matches your image will
be generated.

%prep

%build

%install
mkdir -p %{buildroot}%{_datadir}/krita/pykrita
cd %{buildroot}%{_datadir}/krita/pykrita
tar xf %{S:0}
%autopatch -p0
find . -name "*.*~" |xargs rm

%files
%{_datadir}/krita/pykrita/*
