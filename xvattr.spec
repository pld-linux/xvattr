Summary:	Getting and setting Xv attributes
Summary(pl.UTF-8):	Odczyt i ustawianie atrybutów Xv
Name:		xvattr
Version:	1.3
Release:	1
License:	GPL
Group:		X11/Applications
Source0:	http://www.dtek.chalmers.se/groups/dvd/dist/%{name}-%{version}.tar.gz
# Source0-md5:	041e0d1f2ebce216e69e08ce78ec2ceb
BuildRequires:	XFree86-devel >= 4.0
BuildRequires:	gtk+-devel >= 0.99.7
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)


%description
This program is used for getting and setting Xv attributes such as
XV_BRIGHTNESS, XV_CONTRAST, XV_SATURATION, XV_HUE, XV_COLORKEY...

%description -l pl.UTF-8
Ten program służy do odczytu i ustawiania atrybutów Xv, takich jak
XV_BRIGHTNESS, XV_CONTRAST, XV_SATURATION, XV_HUE, XV_COLORKEY...

%package gtk
Summary:	GTK+ interface for getting and setting Xv attributes
Summary(pl.UTF-8):	Interfejs GTK+ do odczytu i ustawiania atrybutów Xv
Group:		X11/Applications

%description gtk
This is GTK+ interface for getting and setting Xv attributes such as
XV_BRIGHTNESS, XV_CONTRAST, XV_SATURATION, XV_HUE, XV_COLORKEY...

%description gtk -l pl.UTF-8
To jest interfejs GTK+ do odczytu i ustawiania atrybutów Xv, takich jak
XV_BRIGHTNESS, XV_CONTRAST, XV_SATURATION, XV_HUE, XV_COLORKEY...

%prep
%setup -q

%build
%configure

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README
%attr(755,root,root) %{_bindir}/xvattr
%{_mandir}/man1/xvattr.1*

%files gtk
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/gxvattr
