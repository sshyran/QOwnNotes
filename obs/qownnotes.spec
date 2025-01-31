#
# Spec file for package qownnotes for openSUSE Linux and Fedora Linux
#
# Check for Linux distribution version numbers here:
# https://en.opensuse.org/openSUSE:Build_Service_cross_distribution_howto
#


Name:           qownnotes
BuildRequires:  gcc gcc-c++ fdupes

# This is for all Fedora
%if 0%{?fedora}

BuildRequires:  qt5-qtbase
BuildRequires:  qt5-qtbase-devel
BuildRequires:  qt5-qtbase-gui
#BuildRequires:  qt5-qtwebkit-devel
BuildRequires:  qt5-qttools qt5-qttools-devel
BuildRequires:  qt5-qtsvg-devel
BuildRequires:  qt5-qtscript-devel
BuildRequires:  desktop-file-utils
Requires:       qt5-qtsvg

%else
# This is for all SUSE

BuildRequires:  libqt5-qtbase-devel libQt5Script-devel libQt5Svg-devel
BuildRequires:  update-desktop-files 
Requires:       libQt5Svg5

%endif

License:        GPL-2.0
Group:          System/GUI/Productivity
Summary:        Note-taking app and todo list manager with ownCloud integration
Url:            http://www.qownnotes.org/
Version:        VERSION-STRING
Release:        1
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
Source0:        %{name}-%{version}.tar.xz


%description
QOwnNotes is the open source notepad and todo list manager, that works together with the default notes application of ownCloud.

So you are able to write down your thoughts with QOwnNotes and edit or search for them later from your mobile device (like with CloudNotes or the ownCloud web-service.

The notes are stored as plain text files and are synced with ownCloud's file sync functionality. Of course other software, like Dropbox can be used too.

I like the concept of having notes accessible in plain text files, like it is done in the ownCloud notes app, to gain a maximum of freedom, but I was not able to find a decent desktop note taking tool or a text editor, that handles them well. Out of this need QOwnNotes was born.

www.qownnotes.org

Author
======
Patrizio Bekerle <patrizio@bekerle.com>


%prep
%setup -q 
mkdir build
pushd build
qmake-qt5 ..
popd

%build
echo centos_version 0%{?centos_version}
echo rhel_version   0%{?rhel_version}
echo fedora 0%{?fedora}
echo suse_version   0%{?suse_version}

pushd build
CFLAGS=$RPM_OPT_FLAGS CCFLAGS=$CFLAGS

%if 0%{?fedora}

make

%else

%make_jobs

%endif

popd

%install
pushd build
install -D -m 0755 QOwnNotes $RPM_BUILD_ROOT/%{_prefix}/bin/QOwnNotes
popd

# manually install desktop file for Fedora
%if 0%{?fedora}
install -D -m 0644 QOwnNotes.desktop $RPM_BUILD_ROOT/%{_datadir}/applications/QOwnNotes.desktop
%endif

install -D -m 0644 images/icons/128x128/QOwnNotes.png $RPM_BUILD_ROOT/%{_datadir}/pixmaps/QOwnNotes.png
install -D -m 0644 images/icons/16x16/QOwnNotes.png $RPM_BUILD_ROOT/%{_datadir}/icons/hicolor/16x16/apps/QOwnNotes.png
install -D -m 0644 images/icons/24x24/QOwnNotes.png $RPM_BUILD_ROOT/%{_datadir}/icons/hicolor/24x24/apps/QOwnNotes.png
install -D -m 0644 images/icons/32x32/QOwnNotes.png $RPM_BUILD_ROOT/%{_datadir}/icons/hicolor/32x32/apps/QOwnNotes.png
install -D -m 0644 images/icons/48x48/QOwnNotes.png $RPM_BUILD_ROOT/%{_datadir}/icons/hicolor/48x48/apps/QOwnNotes.png
install -D -m 0644 images/icons/64x64/QOwnNotes.png $RPM_BUILD_ROOT/%{_datadir}/icons/hicolor/64x64/apps/QOwnNotes.png
install -D -m 0644 images/icons/96x96/QOwnNotes.png $RPM_BUILD_ROOT/%{_datadir}/icons/hicolor/96x96/apps/QOwnNotes.png
install -D -m 0644 images/icons/128x128/QOwnNotes.png $RPM_BUILD_ROOT/%{_datadir}/icons/hicolor/128x128/apps/QOwnNotes.png
install -D -m 0644 images/icons/256x256/QOwnNotes.png $RPM_BUILD_ROOT/%{_datadir}/icons/hicolor/256x256/apps/QOwnNotes.png
install -D -m 0644 images/icons/512x512/QOwnNotes.png $RPM_BUILD_ROOT/%{_datadir}/icons/hicolor/512x512/apps/QOwnNotes.png
install -D -m 0644 languages/QOwnNotes_en.qm $RPM_BUILD_ROOT/%{_datadir}/QOwnNotes/languages/QOwnNotes_en.qm
install -D -m 0644 languages/QOwnNotes_de.qm $RPM_BUILD_ROOT/%{_datadir}/QOwnNotes/languages/QOwnNotes_de.qm
install -D -m 0644 languages/QOwnNotes_fr.qm $RPM_BUILD_ROOT/%{_datadir}/QOwnNotes/languages/QOwnNotes_fr.qm
install -D -m 0644 languages/QOwnNotes_pl.qm $RPM_BUILD_ROOT/%{_datadir}/QOwnNotes/languages/QOwnNotes_pl.qm
install -D -m 0644 languages/QOwnNotes_zh.qm $RPM_BUILD_ROOT/%{_datadir}/QOwnNotes/languages/QOwnNotes_zh.qm
install -D -m 0644 languages/QOwnNotes_ru.qm $RPM_BUILD_ROOT/%{_datadir}/QOwnNotes/languages/QOwnNotes_ru.qm
install -D -m 0644 languages/QOwnNotes_pt.qm $RPM_BUILD_ROOT/%{_datadir}/QOwnNotes/languages/QOwnNotes_pt.qm
install -D -m 0644 languages/QOwnNotes_es.qm $RPM_BUILD_ROOT/%{_datadir}/QOwnNotes/languages/QOwnNotes_es.qm
install -D -m 0644 languages/QOwnNotes_nl.qm $RPM_BUILD_ROOT/%{_datadir}/QOwnNotes/languages/QOwnNotes_nl.qm
install -D -m 0644 languages/QOwnNotes_hu.qm $RPM_BUILD_ROOT/%{_datadir}/QOwnNotes/languages/QOwnNotes_hu.qm

%if 0%{?suse_version}
%suse_update_desktop_file -c  QOwnNotes QOwnNotes QOwnNotes QOwnNotes QOwnNotes "Utility;SyncUtility;"
%endif

%fdupes $RPM_BUILD_ROOT/%{_prefix}

%clean  
rm -rf $RPM_BUILD_ROOT  

%files
%defattr(-,root,root)
%doc LICENSE README.md CHANGELOG.md SHORTCUTS.md
%{_bindir}/QOwnNotes
%{_datadir}/pixmaps/QOwnNotes.png

%{_datadir}/icons/hicolor/16x16/apps/QOwnNotes.png
%{_datadir}/icons/hicolor/24x24/apps/QOwnNotes.png
%{_datadir}/icons/hicolor/32x32/apps/QOwnNotes.png
%{_datadir}/icons/hicolor/48x48/apps/QOwnNotes.png
%{_datadir}/icons/hicolor/64x64/apps/QOwnNotes.png
%{_datadir}/icons/hicolor/96x96/apps/QOwnNotes.png
%{_datadir}/icons/hicolor/128x128/apps/QOwnNotes.png
%{_datadir}/icons/hicolor/256x256/apps/QOwnNotes.png
%{_datadir}/icons/hicolor/512x512/apps/QOwnNotes.png
%{_datadir}/QOwnNotes/languages/QOwnNotes_en.qm
%{_datadir}/QOwnNotes/languages/QOwnNotes_de.qm
%{_datadir}/QOwnNotes/languages/QOwnNotes_fr.qm
%{_datadir}/QOwnNotes/languages/QOwnNotes_pl.qm
%{_datadir}/QOwnNotes/languages/QOwnNotes_zh.qm
%{_datadir}/QOwnNotes/languages/QOwnNotes_ru.qm
%{_datadir}/QOwnNotes/languages/QOwnNotes_pt.qm
%{_datadir}/QOwnNotes/languages/QOwnNotes_es.qm
%{_datadir}/QOwnNotes/languages/QOwnNotes_nl.qm
%{_datadir}/QOwnNotes/languages/QOwnNotes_hu.qm
%{_datadir}/applications/QOwnNotes.desktop

%dir %{_datadir}/icons/hicolor/512x512/apps
%dir %{_datadir}/icons/hicolor/256x256/apps
%dir %{_datadir}/icons/hicolor/128x128/apps
%dir %{_datadir}/icons/hicolor/96x96/apps
%dir %{_datadir}/icons/hicolor/64x64/apps
%dir %{_datadir}/icons/hicolor/48x48/apps
%dir %{_datadir}/icons/hicolor/32x32/apps
%dir %{_datadir}/icons/hicolor/24x24/apps
%dir %{_datadir}/icons/hicolor/16x16/apps
%dir %{_datadir}/icons/hicolor/512x512
%dir %{_datadir}/icons/hicolor/256x256
%dir %{_datadir}/icons/hicolor/128x128
%dir %{_datadir}/icons/hicolor/96x96
%dir %{_datadir}/icons/hicolor/64x64
%dir %{_datadir}/icons/hicolor/48x48
%dir %{_datadir}/icons/hicolor/32x32
%dir %{_datadir}/icons/hicolor/24x24
%dir %{_datadir}/icons/hicolor/16x16
%dir %{_datadir}/icons/hicolor
%dir %{_datadir}/QOwnNotes/languages
%dir %{_datadir}/QOwnNotes

%changelog



