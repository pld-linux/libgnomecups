Summary:	GNOME CUPS library
Summary(pl):	Biblioteka GNOME CUPS
Name:		libgnomecups
Version:	0.2.2
Release:	2
License:	GPL
Group:		Libraries
Source0:	http://ftp.gnome.org/pub/gnome/sources/libgnomecups/0.2/%{name}-%{version}.tar.bz2
# Source0-md5:	959d5524fe9c37efb55ccfa02e3a063b
URL:		http://www.gnome.org/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	cups-devel
BuildRequires:	gettext-devel
BuildRequires:	glib2-devel >= 1:2.6.3
BuildRequires:	gnome-common >= 2.8.0
BuildRequires:	intltool
BuildRequires:	libtool
BuildRequires:	openssl-devel >= 0.9.7d
BuildRequires:	pkgconfig
BuildRequires:	rpmbuild(macros) >= 1.197
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
GNOME CUPS library - wrapper for CUPS library.

%description -l pl
Biblioteka GNOME CUPS - bêd±ca interfejsem do biblioteki CUPS.

%package devel
Summary:	Devel files for libgnomecups
Summary(pl):	Pliki nag³ówkowe libgnomecups
Group:		Development/Libraries
Requires:	cups-devel
Requires:	%{name} = %{version}-%{release}
Requires:	glib2-devel
Requires:	openssl-devel >= 0.9.7d

%description devel
Devel files for libgnomecups.

%description devel -l pl
Pliki nag³ówkowe libgnomecups.

%package static
Summary:	libgnomecups static library
Summary(pl):	Statyczna biblioteka libgnomecups
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
libgnomecups static library.

%description static -l pl
Statyczna biblioteka libgnomecups.

%prep
%setup -q

%build
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__automake}
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

rm -r $RPM_BUILD_ROOT%{_datadir}/locale/no

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog
%attr(755,root,root) %{_libdir}/libgnomecups*.so.*.*.*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libgnomecups*.so
%{_libdir}/libgnomecups*.la
%{_includedir}/%{name}-1
%{_pkgconfigdir}/%{name}*.pc

%files static
%defattr(644,root,root,755)
%{_libdir}/libgnomecups*.a
