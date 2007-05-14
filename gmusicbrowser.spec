%define name	gmusicbrowser
%define version	0.9550
%define shortversion 0.955
%define release %mkrel 1

Name: 	 	%{name}
Summary: 	Jukebox for collections of music files
Version: 	%{version}
Release: 	%{release}

Source:		http://squentin.free.fr/gmusicbrowser/%{name}-%{shortversion}.tar.bz2
URL:		http://squentin.free.fr/gmusicbrowser/gmusicbrowser.html
License:	GPL
Group:		Sound
BuildRoot:	%{_tmppath}/%{name}-buildroot
BuildRequires:	ImageMagick
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
rm -rf $RPM_BUILD_ROOT
make install prefix=%{buildroot}%{_prefix}

#menu
mkdir -p $RPM_BUILD_ROOT%{_menudir}
cat << EOF > $RPM_BUILD_ROOT%{_menudir}/%{name}
?package(%{name}): command="%{name}" icon="%{name}.png" needs="x11" title="GMusicBrowser" longtitle="Music Collection Jukebox" section="Multimedia/Sound" xdg="true"
EOF

desktop-file-install --vendor="" \
  --remove-category="Application" \
  --add-category="X-MandrivaLinux-Multimedia-Sound;AudioVideo;Audio;Player" \
  --dir $RPM_BUILD_ROOT%{_datadir}/applications $RPM_BUILD_ROOT%{_datadir}/applications/*

rm -rf %{buildroot}%{datadir}/doc/%{name}-%{shortversion}

%find_lang %name

%clean
rm -rf $RPM_BUILD_ROOT

%post
%{update_desktop_database}
		
%postun
%{clean_desktop_database}

%files -f %{name}.lang
%defattr(-,root,root)
%{_datadir}/doc/*
%{_bindir}/%name
%{_datadir}/%name
%{_datadir}/applications/*.desktop
%{_mandir}/man1/*
%{_menudir}/%name
%{_liconsdir}/%name.png
%{_iconsdir}/%name.png
%{_miconsdir}/%name.png
