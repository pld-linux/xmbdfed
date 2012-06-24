Summary:	Motif-based BDF, Linux console (PSF, CP, and FNT) font editor
Summary(pl):	Edytor font�w bazuj�cych na Motifie BDF, Linuxowej konsoli (PSF, CP, i FNT)
Name:		xmbdfed
Version:	4.4
Release:	4
License:	Distributable
Group:		X11/Applications
Group(de):	X11/Applikationen
Group(pl):	X11/Aplikacje
Source0:	ftp://crl.nmsu.edu/CLR/multiling/General/%{name}-%{version}.tar.gz
Source1:	%{name}.desktop
BuildRequires:	XFree86-devel
BuildRequires:	freetype1-devel
BuildRequires:	motif-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define 	_prefix		/usr/X11R6
%define 	_mandir 	%{_prefix}/man

%description
XmBDFEditor is a Motif-based BDF font editor with the following
features:
  - Multiple fonts can be loaded from the command line.
  - Multiple fonts can be open at the same time.
  - Cutting and pasting glyphs between fonts.
  - Multiple glyph bitmap editors can be open at the same time.
  - Cutting and pasting between glyph bitmap editors.
  - Export of XBM files from glyph bitmap editors.
  - Automatic correction of certain metrics when a font is loaded.
  - Generation of XLFD font names for fonts without XLFD names.
  - Update an XLFD font name from the font properties.
  - Update the font properties from an XLFD font name.
  - Font property editor.
  - Font comment editor.
  - Supports unencoded glyphs (ENCODING of -1).
  - Display of glyph encodings in octal, decimal, or hex.
  - Builtin on-line help.
  - Imports PK/GF fonts.
  - Imports HBF (Han Bitmap Font) fonts.
  - Imports Linux console fonts (PSF, CP, and FNT).
  - Imports Sun console fonts (vfont format).
  - Imports fonts from the X server.
  - Imports Windows FON/FNT fonts.
  - Imports TrueType fonts and collections.
  - Exports PSF fonts.
  - Exports HEX fonts.
  - Edits two and four bits per pixel gray scale fonts.

%description -l pl
XmBDFEditor jest bazuj�cym na Motifie BDF edytorem font�w z
ulepszeniami:
  - Kilka font�w r�wnocze�nie mo�e by� za�adowanych z lini komend.
  - Kilka font�w mo�e by� otwartych r�wnocze�nie.
  - Wycinanie i wklejanie glyphs�w pomi�dzy fontami.
  - Kilka edytor�w glyph bitmap mo�e by� otwartych r�wnocze�nie.
  - Wycinanie i wklejanie pomi�dzy edytorami glyph bitmap.
  - Automatyczna korekcja miar podczas �adowania fontu.
  - Generacjia nazw XLFD dla font�w bez takich nazw.
  - Aktualizacja nazw font�w XLFD w w�a�ciwo�ciach fontu.
  - Aktualizacjia w�a�ciwo�ci fontu na podstaiwe nazwy fontu XLFD.
  - Edytor w�a�ciwo�ci fontur.
  - Edytor komentarzy font�w.
  - Wsparcie dla niezakodowanych glyphs�w (KODOWANIE z -1).
  - Wy�wietlanie kodowania glyph�w �semkowo, decymalnie lub
    heksadecymalnie.
  - Wbudowana pomoc.
  - Importowanie font�w PK/GF.
  - Importowanie font�w HBF (Han Bitmap Font).
  - Importowanie Linuxowych font�w konsolowych (PSF, CP, i FNT).
  - Importowanie font�w konsolowych Suna (format vfont).
  - Importowanie font�w z X serwera.
  - Importowanie font�w Windows FON/FNT.
  - Importowanie font�w TrueType i ich kolekcji.

%prep
%setup -q

%build
make	HBFDEFS="-Dunix -DIN_MEMORY -DGUNZIP_CMD=\"/bin/gunzip -c\"" \
	INCS="-I/usr/X11R6/include -I/usr/include/freetype" \
	LIBS="-L/usr/X11R6/lib -lXm -lXpm -lXmu -lXt -lX11 -lSM -lICE -lttf" \
	FTYPE_DEFS="-DHAVE_FREETYPE" \
	CFLAGS="%{?debug:-O0 -g}%{!?debug:$RPM_OPT_FLAGS} -Wall"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_mandir}/man1} \
	$RPM_BUILD_ROOT%{_applnkdir}/Development/Editors

install %{name} $RPM_BUILD_ROOT%{_bindir}
install %{name}.man $RPM_BUILD_ROOT%{_mandir}/man1/%{name}.1
install %{SOURCE1} $RPM_BUILD_ROOT%{_applnkdir}/Development/Editors

gzip -9nf README COPYRIGHTS

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc {README,COPYRIGHTS}.gz
%attr(755,root,root) %{_bindir}/%{name}

%{_mandir}/man1/*
%{_applnkdir}/Development/Editors/xmbdfed.desktop
