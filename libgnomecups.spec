Summary:	libgnomecups
Name:		libgnomecups
Version:	0.1.4
Release:	0.9
License:	GPL
Group:		Libraries
Source0:	http://ftp.gnome.org/pub/gnome/sources/%{name}/0.1/%{name}-%{version}.tar.bz2
# Source0-md5:	26a3fb43696ea6c0973e7a16307fa819
URL:		http://www.gnome.org/
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
libgnomecups.

%package devel
Summary:	Devel files for libgnomecups
Group:		Development/Libraries
Requires:	%{name} = %{version}

%description devel
Devel files for libgnomecups.

%package static
Summary:	libgnomecups static library
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}

%description static
libgnomecups static library.

%prep
%setup -q

%build
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libgnomecups*.so.*.*.*

%files devel
%defattr(644,root,root,755)
%{_includedir}/%{name}-1
%{_libdir}/libgnomecups*.la
%{_libdir}/libgnomecups*.so
%{_pkgconfigdir}/%{name}*.pc

%files static
%defattr(644,root,root,755)
%{_libdir}/libgnomecups*.a
