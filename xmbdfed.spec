Summary:	Motif-based BDF, Linux console (PSF, CP, and FNT) font editor
Summary(pl):	Edytor font�w bazuj�cych na Motifie BDF, Linuxowej konsoli (PSF, CP, i FNT)
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
XmBDFEditor jest bazuj�cym na Motifie BDF edytorem font�w z ulepszeniami:
  o  Kilka font�w r�wnocze�nie mo�e by� za�adowanych z lini komend.
  o  Kilka font�w mo�e by� otwartych r�wnocze�nie.
  o  Wycinanie i wklejanie glyphs�w pomi�dzy fontami.
  o  Kilka edytor�w glyph bitmap mo�e by� otwartych r�wnocze�nie.
  o  Wycinanie i wklejanie pomi�dzy edytorami glyph bitmap.
  o  Automatyczna korekcja miar podczas �adowania fontu.
  o  Generacjia nazw XLFD dla font�w bez takich nazw.
  o  Aktualizacja nazw font�w XLFD w w�a�ciwo�ciach fontu.
  o  Aktualizacjia w�a�ciwo�ci fontu na podstaiwe nazwy fontu XLFD.
  o  Edytor w�a�ciwo�ci fontur.
  o  Edytor komentarzy font�w.
  o  Wsparcie dla niezakodowanych glyphs�w (KODOWANIE z -1).
  o  Wy�wietlanie kodowania glyph�w �semkowo, decymalnie lub heksadecymalnie.
  o  Wbudowana pomoc.
  o  Importowanie font�w PK/GF.
  o  Importowanie font�w HBF (Han Bitmap Font).
  o  Importowanie Linuxowych font�w konsolowych (PSF, CP, i FNT).
  o  Importowanie font�w konsolowych Suna (format vfont).
  o  Importowanie font�w z X serwera.
  o  Importowanie font�w Windows FON/FNT.
  o  Importowanie font�w TrueType i ich kolekcji.

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
