Summary:	SSH X11 passphrase dialog
Summary(de.UTF-8):	SSH X11 Passwort-Dialog
Summary(es.UTF-8):	Diálogo para introducción de passphrase para X11
Summary(fr.UTF-8):	Dialogue pass-phrase X11 d'SSH
Summary(it.UTF-8):	Finestra di dialogo X11 per la frase segreta di SSH
Summary(pl.UTF-8):	Odpytywacz hasła SSH dla X11
Summary(pt.UTF-8):	Diálogo de pedido de senha para X11 do SSH
Summary(pt_BR.UTF-8):	Diálogo para entrada de passphrase para X11
Summary(ru.UTF-8):	SSH - диалог ввода ключевой фразы (passphrase) для X11
Summary(uk.UTF-8):	SSH - діалог вводу ключової фрази (passphrase) для X11
Name:		ssh-askpass-fullscreen
Version:	0.4
Release:	2
License:	GPL v2
Group:		Applications/Networking
Source0:	http://www.cgabriel.org/download/ssh-askpass-fullscreen/%{name}-%{version}.tar.gz
# Source0-md5:	989b2c34b4a43ae0117ce69d464a417d
URL:		https://trac.cgabriel.org/wiki/SshAskpassFullscreen
BuildRequires:	gtk+2-devel >= 2.0.0
BuildRequires:	pkgconfig
Requires:	openssh
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This is an X11-based passphrase dialog for use with SSH.

%description -l es.UTF-8
Este paquete contiene un programa que abre una caja de diálogo para
entrada de passphrase en X11.

%description -l pl.UTF-8
To jest bazujący na X11 odpytywacz hasła do użytku z SSH.

%description -l pt_BR.UTF-8
Esse pacote contém um programa que abre uma caixa de diálogo para
entrada de passphrase no X11.

%description -l ru.UTF-8
Ssh (Secure Shell) - это программа для "захода" (login) на удаленную
машину и для выполнения команд на удаленной машине.

Этот пакет содержит диалог ввода ключевой фразы для использования под
X11.

%description -l uk.UTF-8
Ssh (Secure Shell) - це програма для "заходу" (login) до віддаленої
машини та для виконання команд на віддаленій машині.

Цей пакет містить діалог вводу ключової фрази для використання під
X11.

%prep
%setup -q

%build
%{__cc} ssh-askpass-fullscreen.c \
	%{rpmcflags} -Wall \
	-o ssh-askpass-fullscreen \
	`pkg-config --libs gtk+-2.0` \
	`pkg-config --cflags gtk+-2.0`

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_bindir}

cp -a ssh-askpass-fullscreen $RPM_BUILD_ROOT%{_bindir}/ssh-askpass-fullscreen

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog README
%attr(755,root,root) %{_bindir}/ssh-askpass-fullscreen
