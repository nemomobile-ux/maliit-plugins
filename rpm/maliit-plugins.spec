# 
# Do NOT Edit the Auto-generated Part!
# Generated by: spectacle version 0.26
# 

Name:       maliit-plugins

# >> macros
# << macros

Summary:    Reference input method plugins
Version:    0.99.0
Release:    1
Group:      System/GUI/Other
License:    LGPLv2.1
URL:        http://gitorious.org/maliit/maliit-plugins
Source0:    %{name}-%{version}.tar.bz2
Requires:   qt5-qtdeclarative-import-qtquick2plugin
Requires:   qt5-qtsvg-plugin-imageformat-svg
Requires:   hunspell
BuildRequires:  pkgconfig(maliit-plugins)
BuildRequires:  pkgconfig(Qt5Core)
BuildRequires:  pkgconfig(Qt5Gui)
BuildRequires:  pkgconfig(Qt5Quick)
BuildRequires:  pkgconfig(Qt5Test)
BuildRequires:  hunspell
BuildRequires:  doxygen

%description
Reference inputmethod plugins, such as the Maliit Keyboard


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

# >> setup
# << setup

%build
unset LD_AS_NEEDED
# >> build pre
# << build pre

%qmake5

make %{?jobs:-j%jobs}

# >> build post
# << build post

%install
rm -rf %{buildroot}
# >> install pre
# << install pre
%qmake_install

# >> install post
# << install post

%files
%defattr(-,root,root,-)
%{_libdir}/maliit/plugins/nemo-keyboard.qml
%{_datadir}/maliit/plugins/org/nemomobile
# >> files
# << files

%files maliit-keyboard
%defattr(-,root,root,-)
%{_bindir}/maliit-keyboard-benchmark
%{_libdir}/maliit/plugins/libmaliit-keyboard-plugin.so
%{_datadir}/maliit/plugins/languages
%{_datadir}/maliit/plugins/org/maliit
# >> files
# << files

%files doc
%defattr(-,root,root,-)
%{_docdir}/maliit-plugins/
# >> files doc
# << files doc
