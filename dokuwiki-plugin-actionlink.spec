%define		snap	2005-05-26
%define		ver	%(echo %{snap} | tr -d -)
%define		plugin		actionlink
Summary:	DokuWiki Actionlink Plugin
Name:		dokuwiki-plugin-%{plugin}
Version:	%{ver}
Release:	1
License:	GPL v2
Group:		Applications/WWW
Source0:	http://mbot.ovh.org/plugin-actionlink-%{snap}.tar.gz
# Source0-md5:	ff45e9631f70d42d5bf405e5090bc999
URL:		http://www.dokuwiki.org/plugin:actionlink
Requires:	dokuwiki
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		dokuconf	/etc/webapps/dokuwiki
%define		dokudir		/usr/share/dokuwiki
%define		plugindir	%{dokudir}/lib/plugins/%{plugin}

%description
This plugin lets you use actionlinks in your wiki syntax. It's based on the
dokuwiki's core function tpl_actionlink().

%prep
%setup -q -n %{plugin}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{plugindir}
cp -a . $RPM_BUILD_ROOT%{plugindir}

%clean
rm -rf $RPM_BUILD_ROOT

%post
# force css cache refresh
if [ -f %{dokuconf}/local.php ]; then
	touch %{dokuconf}/local.php
fi

%files
%defattr(644,root,root,755)
%dir %{plugindir}
%{plugindir}/syntax.php
