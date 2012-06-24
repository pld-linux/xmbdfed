# TODO: fix amd64 build and 64-bit pointer handling
#
Summary:	Motif-based BDF, Linux console (PSF, CP, and FNT) font editor
Summary(pl):	Bazuj�cy na Motifie edytor font�w BDF, linuksowej konsoli (PSF, CP, i FNT)
Name:		xmbdfed
Version:	4.5
Release:	5
License:	distributable
Group:		X11/Applications
Source0:	ftp://crl.nmsu.edu/CLR/multiling/General/%{name}-%{version}.tar.gz
# Source0-md5:	8420d39931a0674784f3fd0c0f1f9d6a
Source1:	%{name}.desktop
Source2:	%{name}.png
Patch0:		%{name}-include.patch
BuildRequires:	XFree86-devel
BuildRequires:	freetype1-devel
BuildRequires:	motif-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

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
XmBDFEditor jest bazuj�cym na Motifie edytorem font�w BDF z
ulepszeniami:
- Kilka font�w r�wnocze�nie mo�e by� za�adowanych z linii komend.
- Kilka font�w mo�e by� otwartych r�wnocze�nie.
- Wycinanie i wklejanie glyphs�w pomi�dzy fontami.
- Kilka edytor�w glyph bitmap mo�e by� otwartych r�wnocze�nie.
- Wycinanie i wklejanie pomi�dzy edytorami glyph bitmap.
- Automatyczna korekcja miar podczas �adowania fontu.
- Generacja nazw XLFD dla font�w bez takich nazw.
- Aktualizacja nazw font�w XLFD w w�a�ciwo�ciach fontu.
- Aktualizacja w�a�ciwo�ci fontu na podstawie nazwy fontu XLFD.
- Edytor w�a�ciwo�ci font�w.
- Edytor komentarzy font�w.
- Wsparcie dla niezakodowanych glyphs�w (KODOWANIE z -1).
- Wy�wietlanie kodowania glyph�w �semkowo, decymalnie lub
  heksadecymalnie.
- Wbudowana pomoc.
- Importowanie font�w PK/GF.
- Importowanie font�w HBF (Han Bitmap Font).
- Importowanie linuksowych font�w konsolowych (PSF, CP, i FNT).
- Importowanie font�w konsolowych Suna (format vfont).
- Importowanie font�w z X serwera.
- Importowanie font�w Windows FON/FNT.
- Importowanie font�w TrueType i ich kolekcji.

%prep
%setup -q
%patch0 -p1

%build
%{__make} \
	HBFDEFS="-Dunix -DIN_MEMORY -DGUNZIP_CMD=\"/bin/gunzip -c\"" \
	INCS="-I/usr/X11R6/include -I/usr/include/freetype" \
	LIBS="-L/usr/X11R6/%{_lib} -lXm -lXpm -lXmu -lXt -lX11 -lSM -lICE -lttf" \
	FTYPE_DEFS="-DHAVE_FREETYPE" \
	CFLAGS="%{rpmcflags} -Wall" \
	CC="%{__cc}"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_mandir}/man1} \
	$RPM_BUILD_ROOT{%{_desktopdir},%{_pixmapsdir}}

install %{name} $RPM_BUILD_ROOT%{_bindir}
install %{name}.man $RPM_BUILD_ROOT%{_mandir}/man1/%{name}.1
install %{SOURCE1} $RPM_BUILD_ROOT%{_desktopdir}
install %{SOURCE2} $RPM_BUILD_ROOT%{_pixmapsdir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README COPYRIGHTS
%attr(755,root,root) %{_bindir}/%{name}
%{_desktopdir}/xmbdfed.desktop
%{_pixmapsdir}/*.png
%{_mandir}/man1/*
