%define name	gmusicbrowser
%define version	0.962
%define shortversion 0.962
%define release %mkrel 2

Name: 	 	%{name}
Summary: 	Jukebox for collections of music files
Version: 	%{version}
Release: 	%{release}
Epoch:          1

Source:		http://squentin.free.fr/gmusicbrowser/%{name}-%{shortversion}.tar.bz2
URL:		http://squentin.free.fr/gmusicbrowser/gmusicbrowser.html
License:	GPL
Group:		Sound
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildRequires:	ImageMagick desktop-file-utils
Requires:	perl-Gtk2 >= 1.090
Requires:	perl-GStreamer >= 0.06
Requires:	gstreamer0.10-plugins-good
Requires:	gstreamer0.10-plugins-ugly
Requires:	gstreamer0.10-flac
Requires:	perl-Gtk2-TrayIcon
Requires:	perl-Gtk2-MozEmbed
BuildArch:	noarch

Requires(post): desktop-file-utils
Requires(postun): desktop-file-utils
%define	_requires_exceptions	perl\(simple_http\)

%description
An open-source jukebox for large collections of mp3/ogg/flac files.
    * fast even with 10,000s of songs (developed with over 16000 songs on a
      duron800)
    * powerful browser which doesn't interfere with the playlist
    * artist/album lock : easily restrict playlist to current artist/album
    * easy access to songs related to the currently playing song
          o songs from the same album
          o album(s) from the same artist(s)
          o songs with same title (other versions, covers, ...)
    * support ogg vorbis, mp3 and flac files (and mpc with gstreamer)
    * fully featured tag editor (support all id3 versions, limited support for
      APE & lyrics3 tags)
    * simple mass-tagging and mass-renaming
    * support multiple genres for a song
    * support multiple artists for each song by separating them with '&'
    * customizable named 'flags' can be set for each song (ex : bootleg, live,
      -'s favorites, ...)
    * filter history in the browser window
    * filters with unlimited nesting of conditions
    * customizable weighted random mode (based on rating, last time played,
      flag, ...)
    * tray icon, with tip window
    * customizable window layouts
    * plugin system (experimental), included plugins :
          o nowplaying (to update an external program when the playing song
            changes)
          o last.fm
          o fetch cover from google image
          o simple lyrics
          o MozEmbed : use the mozilla engine to display wikipedia artist page
            and search lyrics with google

%prep
%setup -qn %{name}-%{shortversion}

%install
rm -rf %{buildroot}
make install prefix=%{buildroot}%{_prefix}

desktop-file-install --vendor="" \
  --remove-category="Application" \
  --add-category="X-MandrivaLinux-Multimedia-Sound;AudioVideo;Audio;Player" \
  --dir %{buildroot}%{_datadir}/applications $RPM_BUILD_ROOT%{_datadir}/applications/*

rm -rf %{buildroot}%{datadir}/doc/%{name}-%{shortversion}
rm -rf %{buildroot}/%{_menudir}

%find_lang %{name}

%post
%{update_desktop_database}

%postun
%{clean_desktop_database}

%clean
rm -rf %{buildroot}

%files -f %{name}.lang
%defattr(-,root,root)
%{_docdir}/*
%{_bindir}/%{name}
%{_datadir}/%{name}
%{_datadir}/applications/*.desktop
%{_mandir}/man1/*
%{_miconsdir}/%{name}.png
%{_iconsdir}/%{name}.png
%{_liconsdir}/%{name}.png
