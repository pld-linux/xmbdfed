Summary:	Motif-based BDF, Linux console (PSF, CP, and FNT) font editor
Summary(pl):	Edytor fontów bazuj±cych na Motifie BDF, Linuxowej konsoli (PSF, CP, i FNT)
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
XmBDFEditor jest bazuj±cym na Motifie BDF edytorem fontów z
ulepszeniami:
  - Kilka fontów równocze¶nie mo¿e byæ za³adowanych z lini komend.
  - Kilka fontów mo¿e byæ otwartych równocze¶nie.
  - Wycinanie i wklejanie glyphsów pomiêdzy fontami.
  - Kilka edytorów glyph bitmap mo¿e byæ otwartych równocze¶nie.
  - Wycinanie i wklejanie pomiêdzy edytorami glyph bitmap.
  - Automatyczna korekcja miar podczas ³adowania fontu.
  - Generacjia nazw XLFD dla fontów bez takich nazw.
  - Aktualizacja nazw fontów XLFD w w³a¶ciwo¶ciach fontu.
  - Aktualizacjia w³a¶ciwo¶ci fontu na podstaiwe nazwy fontu XLFD.
  - Edytor w³a¶ciwo¶ci fontur.
  - Edytor komentarzy fontów.
  - Wsparcie dla niezakodowanych glyphsów (KODOWANIE z -1).
  - Wy¶wietlanie kodowania glyphów ósemkowo, decymalnie lub
    heksadecymalnie.
  - Wbudowana pomoc.
  - Importowanie fontów PK/GF.
  - Importowanie fontów HBF (Han Bitmap Font).
  - Importowanie Linuxowych fontów konsolowych (PSF, CP, i FNT).
  - Importowanie fontów konsolowych Suna (format vfont).
  - Importowanie fontów z X serwera.
  - Importowanie fontów Windows FON/FNT.
  - Importowanie fontów TrueType i ich kolekcji.

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
