Summary:   Motif-based BDF, Linux console (PSF, CP, and FNT) font editor
Name:      xmbdfed
Version:   3.2
Release:   1
Copyright: 1996, 1997 Computing Research Labs, New Mexico State University
Group:     Development/X11
Source0:   ftp://crl.nmsu.edu/CLR/multiling/General/%{name}-%{version}.tar.gz
Source1:   %{name}.wmconfig
BuildRoot: /tmp/%{name}-%{version}-root
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

%prep
%setup -q

rm -rf $RPM_BUILD_ROOT

%build
make	HBFDEFS="-Dunix -DIN_MEMORY -DGUNZIP_CMD=\"/bin/gunzip -c\"" \
	INCS="-I/usr/X11R6/include" \
	LIBS="-L/usr/X11R6/lib -lXm -lXpm -lXmu -lXt -lX11 -lSM -lICE -lttf" \
	FTYPE_DEFS="-DHAVE_FREETYPE" \
	CFLAGS="$RPM_OPT_FLAGS -Wall"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT/{etc/X11/wmconfig,usr/X11R6/{bin,man/man1}}

install -s xmbdfed $RPM_BUILD_ROOT/usr/X11R6/bin
install xmbdfed.man $RPM_BUILD_ROOT/usr/X11R6/man/man1/xmbdfed.1

install %{SOURCE1} $RPM_BUILD_ROOT/etc/X11/wmconfig/xmbdfed

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644, root, root, 755)
%doc README COPYRIGHTS
%config(missingok) /etc/X11/wmconfig/xmbdfed
%attr(755, root, root) /usr/X11R6/bin/xmbdfed
%attr(644, root,  man) /usr/X11R6/man/man1/xmbdfed.1

%changelog
* Wed May 20 1998 Tomasz K這czko <kloczek@rudy.mif.pg.gda.pl>
  [3.0-1]
- %%{version} macro instead %%{PACKAGE_VERSION},
- added support for Imports TrueType fonts,
- removed patching Makefile (now all is passed as make parameters),
- added using $RPM_OPT_FLAGS during compilation,
- added wmconfig registration file,
- added -q %setup parameter,
- added using %%{name} macro in Buildroot,
- "rm -rf $RPM_BUILD_ROOT" added on staret %install,
- added %clean section,
- removed Packager field from spec (if you want recompile package and
  redistribute this package later put this in your private .rpmrc). 
- added %defattr and %attr macros in %files (allows building package from
  non-root account). This require on rebuild rpm >= 2.4.99 but recomended is
  rpm >= 2.5.

* Fri Sep 26 1997 Tomasz K這czko <kloczek@idk.ocm.pl>
  [2.3-1]
- changer %description,

* Mon Sep 15 1997 Tomasz K這czko <kloczek@idk.ocm.pl>
  [2.2-2]
- chenged %attr in %doc to (-, root, root),

* Wed Jul 23 1997 Tomasz K這czko <kloczek@rudy.mif.pg.gda.pl>
  [2.2-1]
- added %%{PACKAGE_VERSION} macro in Source,
- anned %attr macro to %doc files,
- changed permision on man page (644,root,root) -> (644, root, man),
- added "rm -rf $RPM_BUILD_ROOT" in %prep.

* Wed May 21 1997 Tomasz K這czko <kloczek@rudy.mif.pg.gda.pl>
  [2.1-1]
- first release in rpm package.
