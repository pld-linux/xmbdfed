Summary:	Motif-based BDF, Linux console (PSF, CP, and FNT) font editor
Summary(pl):	Edytor fontów bazuj±cych na Motifie BDF, Linuxowej konsoli (PSF, CP, i FNT)
Name:		xmbdfed
Version:	3.8
Release:	1
Copyright:	1996, 1997 Computing Research Labs, New Mexico State University
Group:		X11/Fonts
Group(pl):	X11/Fonty
Source0:	ftp://crl.nmsu.edu/CLR/multiling/General/%{name}-%{version}.tar.gz
Source1:	xmbdfed.wmconfig
BuildRequires:	freetype-devel
BuildRequires:	XFree86-devel
BuildRequires:	xpm-devel
BuildRequires:	lesstif-devel
BuildRoot:	/tmp/%{name}-%{version}-root

%define 	_prefix		/usr/X11R6
%define 	_mandir 	%{_prefix}/man

%description
XmBDFEditor is a Motif-based BDF font editor with the following features:
  o  Multiple fonts can be loaded from the command line.
  o  Multiple fonts can be open at the same time.
  o  Cutting and pasting glyphs between fonts.
  o  Multiple glyph bitmap editors can be open at the same time.
  o  Cutting and pasting between glyph bitmap editors.
  o  Automatic correction of certain metrics when a font is loaded.
  o  Generation of XLFD font names for fonts without XLFD names.
  o  Update an XLFD font name from the font properties.
  o  Update the font properties from an XLFD font name.
  o  Font property editor.
  o  Font comment editor.
  o  Supports unencoded glyphs (ENCODING of -1).
  o  Display of glyph encodings in octal, decimal, or hex.
  o  Builtin on-line help.
  o  Imports PK/GF fonts.
  o  Imports HBF (Han Bitmap Font) fonts.
  o  Imports Linux console fonts (PSF, CP, and FNT).
  o  Imports Sun console fonts (vfont format).
  o  Imports fonts from the X server.
  o  Imports Windows FON/FNT fonts.
  o  Imports TrueType fonts and collections.

%description -l pl
XmBDFEditor jest bazuj±cym na Motifie BDF edytorem fontów z ulepszeniami:
  o  Kilka fontów równocze¶nie mo¿e byæ za³adowanych z lini komend.
  o  Kilka fontów mo¿e byæ otwartych równocze¶nie.
  o  Wycinanie i wklejanie glyphsów pomiêdzy fontami.
  o  Kilka edytorów glyph bitmap mo¿e byæ otwartych równocze¶nie.
  o  Wycinanie i wklejanie pomiêdzy edytorami glyph bitmap.
  o  Automatyczna korekcja miar podczas ³adowania fontu.
  o  Generacjia nazw XLFD dla fontów bez takich nazw.
  o  Aktualizacja nazw fontów XLFD w w³a¶ciwo¶ciach fontu.
  o  Aktualizacjia w³a¶ciwo¶ci fontu na podstaiwe nazwy fontu XLFD.
  o  Edytor w³a¶ciwo¶ci fontur.
  o  Edytor komentarzy fontów.
  o  Wsparcie dla niezakodowanych glyphsów (KODOWANIE z -1).
  o  Wy¶wietlanie kodowania glyphów ósemkowo, decymalnie lub heksadecymalnie.
  o  Wbudowana pomoc.
  o  Importowanie fontów PK/GF.
  o  Importowanie fontów HBF (Han Bitmap Font).
  o  Importowanie Linuxowych fontów konsolowych (PSF, CP, i FNT).
  o  Importowanie fontów konsolowych Suna (format vfont).
  o  Importowanie fontów z X serwera.
  o  Importowanie fontów Windows FON/FNT.
  o  Importowanie fontów TrueType i ich kolekcji.

%prep
%setup -q

%build
make	HBFDEFS="-Dunix -DIN_MEMORY -DGUNZIP_CMD=\"/bin/gunzip -c\"" \
	INCS="-I/usr/X11R6/include" \
	LIBS="-L/usr/X11R6/lib -lXm -lXpm -lXmu -lXt -lX11 -lSM -lICE -lttf" \
	FTYPE_DEFS="-DHAVE_FREETYPE" \
	CFLAGS="$RPM_OPT_FLAGS -Wall"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_mandir}/man1} \
	$RPM_BUILD_ROOT/etc/X11/wmconfig

install -s %{name} $RPM_BUILD_ROOT%{_bindir}
install %{name}.man $RPM_BUILD_ROOT%{_mandir}/man1/%{name}.1

install %{SOURCE1} $RPM_BUILD_ROOT/etc/X11/wmconfig/%{name}

gzip -9nf $RPM_BUILD_ROOT%{_mandir}/man1/* \
	README COPYRIGHTS

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc {README,COPYRIGHTS}.gz
%attr(755,root,root) %{_bindir}/%{name}

/etc/X11/wmconfig/%{name}
%{_mandir}/man1/*
