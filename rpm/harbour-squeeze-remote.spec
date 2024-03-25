# 
# Do NOT Edit the Auto-generated Part!
# Generated by: spectacle version 0.32
# 

Name:       harbour-squeeze-remote

# >> macros
# << macros

%{!?qtc_qmake:%define qtc_qmake %qmake}
%{!?qtc_qmake5:%define qtc_qmake5 %qmake5}
%{!?qtc_make:%define qtc_make make}
%{?qtc_builddir:%define _builddir %qtc_builddir}
Summary:    SqueezeR-emote
Version:    3.2.0
Release:    0
Group:      Qt/Qt
License:    GPLv3
URL:        https://openrepos.net/PawelSpoon/harbour-squeeze-remote
Source0:    %{name}-%{version}.tar.bz2
Source100:  harbour-squeeze-remote.yaml
Requires:   sailfishsilica-qt5 >= 0.10.9
BuildRequires:  pkgconfig(sailfishapp) >= 1.0.2
BuildRequires:  pkgconfig(Qt5Core)
BuildRequires:  pkgconfig(Qt5Qml)
BuildRequires:  pkgconfig(Qt5Quick)
BuildRequires:  desktop-file-utils
BuildRequires:  qt5-qttools-linguist
%description
Native remote control for logitech media server aka squeeze server.

You can find more details on a raspberry pie based player and server here:
 https://www.picoreplayer.org 

Openrepos: https://openrepos.net/content/pawelspoon/squeezeremote
Github: https://github.com/PawelSpoon/harbour-squeeze-remote


PackageName: harbour-squeeze-remote
Type: desktop-application
Icon: https://raw.githubusercontent.com/PawelSpoon/harbour-squeeze-remote/master/icons/172x172/harbour-squeeze-remote.png
Screenshots:
  - https://raw.githubusercontent.com/PawelSpoon/harbour-squeeze-remote/master/screenshots/Bildschirmfoto_20220106_001.png
Categories:
  - Multimedia

%prep
%setup -q -n %{name}-%{version}

# >> setup
# << setup

%build
# >> build pre
# << build pre

%qtc_qmake5 

%qtc_make %{?_smp_mflags}

# >> build post
# << build post

%install
rm -rf %{buildroot}
# >> install pre
# << install pre
%qmake5_install

# >> install post
# << install post

desktop-file-install --delete-original       \
  --dir %{buildroot}%{_datadir}/applications             \
   %{buildroot}%{_datadir}/applications/*.desktop

%files
%defattr(-,root,root,-)
%{_bindir}
%{_datadir}/%{name}
%{_datadir}/applications/%{name}.desktop
%{_datadir}/icons/hicolor/*/apps/%{name}.png
# >> files
# << files
