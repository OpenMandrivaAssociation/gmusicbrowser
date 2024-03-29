%if %{_use_internal_dependency_generator}
%define __noautoreq 'perl\\(Gtk2::(.*)\\)'
%endif

Summary:	Jukebox for collections of music files
Name:		gmusicbrowser
Version:	1.1.16
Release:	2
License:	GPLv3+
Group:		Sound
URL:		https://gmusicbrowser.org
Source0:	https://gmusicbrowser.org/download/%{name}-%{version}.tar.gz
BuildRequires:	imagemagick
BuildRequires:	desktop-file-utils
Requires:	perl-Gtk2 >= 1.090
Requires:	perl-GStreamer >= 0.06
Requires:	gstreamer0.10-plugins-good
Requires:	gstreamer0.10-plugins-ugly
Requires:	gstreamer0.10-flac
Requires:	perl-Gtk2-TrayIcon
Requires:	perl-Gtk2-WebKit
Requires:	perl(GStreamer::Interfaces)
Requires:	perl(Net::DBus)
Requires:	vorbis-tools
Requires:	mpg123
Suggests:	gstreamer0.10-lame
BuildArch:	noarch

%description
An open-source jukebox for large collections of mp3/ogg/flac/mpc/ape
files, written in perl.

%files -f %{name}.lang
%doc AUTHORS README NEWS layout_doc.html
%{_bindir}/%{name}
%{_datadir}/%{name}
%{_datadir}/applications/*.desktop
%{_mandir}/man1/*
%{_iconsdir}//hicolor/*/apps/gmusicbrowser.*
%{_metainfodir}/org.gmusicbrowser.metainfo.xml

#---------------------------------------------------------------------------

%prep
%autosetup -p1

%install
%make_install

desktop-file-install \
  --add-category="GTK;Player" \
  --dir %{buildroot}%{_datadir}/applications %{buildroot}%{_datadir}/applications/*

rm -rf %{buildroot}%{_docdir}/%{name}-%{version}
rm -rf %{buildroot}%{_menudir}

%find_lang %{name}
