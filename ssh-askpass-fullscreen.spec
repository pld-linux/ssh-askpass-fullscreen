Summary:	SSH X11 passphrase dialog
Summary(de):	SSH X11 Passwort-Dialog
Summary(es):	DiАlogo para introducciСn de passphrase para X11
Summary(fr):	Dialogue pass-phrase X11 d'SSH
Summary(it):	Finestra di dialogo X11 per la frase segreta di SSH
Summary(pl):	Odpytywacz hasЁa SSH dla X11
Summary(pt):	DiАlogo de pedido de senha para X11 do SSH
Summary(pt_BR):	DiАlogo para entrada de passphrase para X11
Summary(ru):	SSH - диалог ввода ключевой фразы (passphrase) для X11
Summary(uk):	SSH - д╕алог вводу ключово╖ фрази (passphrase) для X11
Name:		ssh-askpass-fullscreen
Version:	0.3
Release:	0.1
License:	GPL v2
Group:		Applications/Networking
Source0:	http://ftp.debian.org/debian/pool/main/s/ssh-askpass-fullscreen/%{name}_%{version}.orig.tar.gz
# Source0-md5:	c46ad80b6bb150270514317001a2cedc
BuildRequires:	gtk+2-devel
Requires:	openssh
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_appdefsdir	/usr/X11R6/lib/X11/app-defaults

%description
This is an X11-based passphrase dialog for use with SSH.

%description -l es
Este paquete contiene un programa que abre una caja de diАlogo para
entrada de passphrase en X11.

%description -l pl
To jest bazuj╠cy na X11 odpytywacz hasЁa do u©ytku z SSH.

%description -l pt_BR
Esse pacote contИm um programa que abre uma caixa de diАlogo para
entrada de passphrase no X11.

%description -l ru
Ssh (Secure Shell) - это программа для "захода" (login) на удаленную
машину и для выполнения команд на удаленной машине.

Этот пакет содержит диалог ввода ключевой фразы для использования под
X11.

%description -l uk
Ssh (Secure Shell) - це програма для "заходу" (login) до в╕ддалено╖
машини та для виконання команд на в╕ддален╕й машин╕.

Цей пакет м╕стить д╕алог вводу ключово╖ фрази для використання п╕д
X11.

%prep
%setup -q

%build
%{__cc} gtk2-ssh-askpass.c \
	%{rpmcflags} -Wall \
	-o gtk2-ssh-askpass \
	`pkg-config --libs gtk+-2.0` \
	`pkg-config --cflags gtk+-2.0`

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_libexecdir}/ssh

install gtk2-ssh-askpass $RPM_BUILD_ROOT%{_libexecdir}/ssh

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog README
%attr(755,root,root) %{_libexecdir}/ssh/*
