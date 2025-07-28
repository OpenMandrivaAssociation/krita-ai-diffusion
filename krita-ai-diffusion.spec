Name:		krita-ai-diffusion
Version:	1.36.1
Release:	1
Source0:	https://github.com/Acly/krita-ai-diffusion/releases/download/v1.36.0/krita_ai_diffusion-%{version}.zip
Summary:	AI image generation plugin for Krita
URL:		https://github.com/Acly/krita-ai-diffusion
License:	GPL
Group:		Graphics
BuildArch:	noarch
BuildRequires:	dos2unix
Requires:	krita >= 6.0.0-0
Supplements:	krita >= 6.0.0-0
Requires:	python-qt6-network
Requires:	python-ensurepip

%patchlist
krita-ai-diffusion-amd-rocm.patch
krita-ai-diffusion-krita-6.0.patch

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
find . -name "*.py" |xargs dos2unix
find . -name "*.py" |xargs sed -i -e 's,PyQt5,PyQt6,g'
%autopatch -p0
find . -name "*.*~" |xargs rm || :

%files
%{_datadir}/krita/pykrita/*
