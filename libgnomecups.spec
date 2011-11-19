Summary:	GNOME CUPS library
Summary(pl.UTF-8):	Biblioteka GNOME CUPS
Name:		libgnomecups
Version:	0.2.3
Release:	3
License:	LGPL v2
Group:		Libraries
Source0:	http://ftp.gnome.org/pub/gnome/sources/libgnomecups/0.2/%{name}-%{version}.tar.bz2
# Source0-md5:	dc4920c15c9f886f73ea74fbff0ae48b
URL:		http://www.gnome.org/
BuildRequires:	autoconf >= 2.52
BuildRequires:	automake
BuildRequires:	cups-devel
BuildRequires:	gettext-devel
BuildRequires:	glib2-devel >= 1:2.12.1
BuildRequires:	gnome-common >= 2.12.0
BuildRequires:	intltool >= 0.20
BuildRequires:	libtool
BuildRequires:	openssl-devel >= 0.9.8b
BuildRequires:	pkgconfig
BuildRequires:	rpmbuild(macros) >= 1.197
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
GNOME CUPS library - wrapper for CUPS library.

%description -l pl.UTF-8
Biblioteka GNOME CUPS - będąca interfejsem do biblioteki CUPS.

%package devel
Summary:	Devel files for libgnomecups
Summary(pl.UTF-8):	Pliki nagłówkowe libgnomecups
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	cups-devel
Requires:	glib2-devel >= 1:2.12.1
Requires:	openssl-devel >= 0.9.8b

%description devel
Devel files for libgnomecups.

%description devel -l pl.UTF-8
Pliki nagłówkowe libgnomecups.

%package static
Summary:	libgnomecups static library
Summary(pl.UTF-8):	Statyczna biblioteka libgnomecups
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
libgnomecups static library.

%description static -l pl.UTF-8
Statyczna biblioteka libgnomecups.

%prep
%setup -q

%build
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

mv -f $RPM_BUILD_ROOT%{_datadir}/locale/{sr@Latn,sr@latin}

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS 
%attr(755,root,root) %{_libdir}/libgnomecups-1.0.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libgnomecups-1.0.so.1

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libgnomecups-1.0.so
%{_libdir}/libgnomecups-1.0.la
%{_includedir}/libgnomecups-1
%{_pkgconfigdir}/libgnomecups-1.0.pc

%files static
%defattr(644,root,root,755)
%{_libdir}/libgnomecups-1.0.a
