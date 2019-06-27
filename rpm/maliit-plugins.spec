Name:       maliit-plugins
Summary:    nemomobile keyboard mallit plugin
Version:    0.99.0
Release:    1
Group:      System/GUI/Other
License:    LGPLv2.1
URL:        https://github.com/nemomobile-ux/maliit-plugins
Source0:    %{name}-%{version}.tar.bz2

Requires:   maliit-framework-wayland
Requires:   qt5-qtdeclarative-import-qtquick2plugin
Requires:   qt5-qtsvg-plugin-imageformat-svg
BuildRequires:  pkgconfig(maliit-plugins)
BuildRequires:  pkgconfig(Qt5Core)
BuildRequires:  pkgconfig(Qt5Gui)
BuildRequires:  pkgconfig(Qt5Quick)
BuildRequires:  pkgconfig(Qt5Test)
BuildRequires:  doxygen

%description
Onscreen keyboard for NemoMobile

%package maliit-keyboard
Summary:    Maliit keyboard plugin
Group:      System/GUI/Other
Requires:   %{name} = %{version}-%{release}

%description maliit-keyboard
Plugin for maliit-server providing maliit styled keyboard

%package doc
Summary:    maliit-plugins documentation
Group:      System/GUI/Other
Requires:   %{name} = %{version}-%{release}

%description doc
Documentation for the maliit-plugins

%prep
%setup -q -n %{name}-%{version}/%{name}

%build
unset LD_AS_NEEDED

%qmake5 CONFIG+=enable-presage
%qmake5 CONFIG+=disable-maliit-keyboard

make %{?jobs:-j%jobs}

%install
rm -rf %{buildroot}
%qmake_install

%files
%defattr(-,root,root,-)
%{_libdir}/maliit/plugins/nemo-keyboard.qml
%{_datadir}/maliit/plugins/org/nemomobile

%files doc
%defattr(-,root,root,-)
%{_docdir}/maliit-plugins/
