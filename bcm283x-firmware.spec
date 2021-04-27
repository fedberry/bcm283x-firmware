#debug packages make no sense!
%global debug_package %{nil}
#no stripping required either
%global __os_install_post %{nil}

%global snap_date       20210427
%global commit_long     616dde8bc8a16dbd524e74ab84f3d3d5663a1641
%global commit_short    %(c=%{commit_long}; echo ${c:0:7})
%global fetch_url       https://raw.githubusercontent.com/raspberrypi/firmware

Name:          bcm283x-firmware
Version:       %{snap_date}
Release:       1.%{commit_short}%{?dist}
Summary:       Broadcom bcm283x firmware for the Raspberry Pi
Group:         System Environment/Kernel
License:       Redistributable, no modification permitted
URL:           https://github.com/raspberrypi/firmware/
Source0:       %{fetch_url}/%{commit_long}/boot/bootcode.bin
Source1:       %{fetch_url}/%{commit_long}/boot/fixup.dat
Source2:       %{fetch_url}/%{commit_long}/boot/fixup_cd.dat
Source3:       %{fetch_url}/%{commit_long}/boot/fixup_db.dat
Source4:       %{fetch_url}/%{commit_long}/boot/fixup_x.dat
Source5:       %{fetch_url}/%{commit_long}/boot/start.elf
Source6:       %{fetch_url}/%{commit_long}/boot/start_cd.elf
Source7:       %{fetch_url}/%{commit_long}/boot/start_db.elf
Source8:       %{fetch_url}/%{commit_long}/boot/start_x.elf
Source9:       %{fetch_url}/%{commit_long}/boot/LICENCE.broadcom
Source10:      %{fetch_url}/%{commit_long}/boot/COPYING.linux
# RPi4 firmware
Source11:      %{fetch_url}/%{commit_long}/boot/fixup4.dat
Source12:      %{fetch_url}/%{commit_long}/boot/fixup4cd.dat
Source13:      %{fetch_url}/%{commit_long}/boot/fixup4db.dat
Source14:      %{fetch_url}/%{commit_long}/boot/fixup4x.dat
Source15:      %{fetch_url}/%{commit_long}/boot/start4.elf
Source16:      %{fetch_url}/%{commit_long}/boot/start4cd.elf
Source17:      %{fetch_url}/%{commit_long}/boot/start4db.elf
Source18:      %{fetch_url}/%{commit_long}/boot/start4x.elf

ExclusiveArch: %{arm} aarch64


%description
GPU (VideoCore IV) firmware for the Broadcom bcm283x SoC used in Raspberry Pi's.


%prep
%setup -c -n %{name}-%{commit_short}
cp -a %{sources} .


%build


%install
mkdir -p %{buildroot}/boot
install -p * %{buildroot}/boot


%files
%license LICENCE.broadcom COPYING.linux
/boot/*


%changelog
* Tue Apr 27 2021 Damian Wrobel <dwrobel@ertelnet.rybnik.pl> - 20210427-1.616dde8
- Sync to latest git commit: 616dde8bc8a16dbd524e74ab84f3d3d5663a1641

* Fri Mar 12 2021 Damian Wrobel <dwrobel@ertelnet.rybnik.pl> - 20210310-1.0591568
- Sync to latest git commit: 0591568b29a724de406aa737fc8e13f68c423f3f

* Wed Dec 23 2020 Damian Wrobel <dwrobel@ertelnet.rybnik.pl> - 20201223-1.0fb9a0d
- Sync to latest git commit: 0fb9a0dce50c3f4683254f57c3a5c20289a4de8a

* Wed Sep 02 2020 Damian Wrobel <dwrobel@ertelnet.rybnik.pl> - 20200901-1.a34f263
- Sync to latest git commit: a34f263ce6a9e35f3c1d62f6195f9f45f4f547e7

* Fri May 29 2020 Damian Wrobel <dwrobel@ertelnet.rybnik.pl> - 20200527-3.62fc8c0
- Sync to latest git commit: 62fc8c01165a80021054a430182b504f7b877c2d

* Sat Apr 01 2020 Damian Wrobel <dwrobel@ertelnet.rybnik.pl> - 20200401-1.c2c6ce8
- Sync to latest git commit: c2c6ce8de2dcfd5a6852a32a16003f25188e52ee

* Mon Mar 09 2020 Damian Wrobel <dwrobel@ertelnet.rybnik.pl> - 20200306-1.163d84c
- Sync to latest git commit: 163d84cbeb7038a4fd71d817eae43a535eb3df62

* Tue Feb 18 2020 Vaughan <devel at agrez dot net> - 20200218-1.f4b5869
- Add aarch64 to ExclusiveArch
- Sync to latest git commit: f4b58692fef0b9c16bd4564edb980fff73a758b3

* Wed Nov 06 2019 Vaughan <devel at agrez dot net> - 20191106-1.b79618b
- Sync to latest git commit: b79618b5db4e4e7c02f9ad9d3ada51713825313e

* Wed Oct 02 2019 Damian Wrobel <dwrobel@ertelnet.rybnik.pl> - 20190930-1.a16470a
- Sync to git commit: a16470ad47c0ad66d5c98d98e08e49cd148c8fc0

* Wed Oct 02 2019 Damian Wrobel <dwrobel@ertelnet.rybnik.pl> - 20190924-1.f5c626c
- Sync to git commit: f5c626c64874d6e1482edf4a76aa22e5e54be63d

* Sat Jul 13 2019 Vaughan <devel at agrez dot net> - 20190713-1.f6d9f13
- Sync to latest git commit: f6d9f139037bf421d5d25b1cebe1a67394542b4b

* Wed Jul 03 2019 Vaughan <devel at agrez dot net> - 20190703-1.383fcf5
- Sync to latest git commit: 383fcf5be7f1bcf8d63ca8b471ecd9b8da3cef0b
- Add RPi4 firmware

* Fri Jun 14 2019 Vaughan <devel at agrez dot net> - 20190614-1.07937c7
- Sync to latest git commit: 07937c7d48bcd44cc1015c6257ae2cfa5da51298

* Sat Mar 30 2019 Vaughan <devel at agrez dot net> - 20190330-1.3dde44c
- Sync to latest git commit: 3dde44c13f17cb34697ef8f867bab147125d5a25

* Tue Mar 19 2019 Vaughan <devel at agrez dot net> - 20190319-1.fd15e07
- Sync to latest git commit: fd15e0700e45d9b7db83e30696aba299b9f2f31d

* Wed Feb 27 2019 Vaughan <devel at agrez dot net> - 20190227-1.f84820e
- Sync to latest git commit: f84820ed7fcfd0f0d364e3d47cdbc83215596b2c

* Sun Feb 03 2019 Vaughan <devel at agrez dot net> - 20190203-1.81cca1a
- Sync to latest git commit: 81cca1a9380c828299e884dba5efd0d4acb39e8d

* Sun Jan 13 2019 Vaughan <devel at agrez dot net> - 20190113-1.9baae76
- Sync to latest git commit: 9baae7655f01ac37ba3b28c0053e9c6d0085dcfb

* Sun Dec 23 2018 Vaughan <devel at agrez dot net> - 20181223-1.e1bd9b0
- Sync to latest git commit: e1bd9b0b8cda901ee9b23cbb8b3334cde71320a7

* Fri Dec 07 2018 Vaughan <devel at agrez dot net> - 20181207-1.077fbe8
- Sync to latest git commit: 077fbe8e06f0264a8fa9886e65aa21486fd7659f

* Sun Nov 25 2018 Vaughan <devel at agrez dot net> - 20181125-1.66be192
- Sync to latest git commit: 66be1927eafd2feed468efd36ec083b208f0a9c3

* Wed Nov 07 2018 Vaughan <devel at agrez dot net> - 20181107-1.55e5912
- Sync to latest git commit: 55e591283f456ab9cebd9c31aaef4939f814880d

* Wed Oct 17 2018 Vaughan <devel at agrez dot net> - 20181017-1.10c1c5f
- Sync to latest git commit: 10c1c5f9637849e8a3a70e114d3837e25987fc7c

* Wed Oct 10 2018 Vaughan <devel at agrez dot net> - 20181010-1.fbad640
- Sync to latest git commit: fbad6408c4596d3d671736ee0571aae444f24e68

* Wed Sep 26 2018 Vaughan <devel at agrez dot net> - 20180926-1.2ecdfe7
- Sync to latest git commit: 2ecdfe7945c8e58b8b94fe142ee0df76fc3f2227

* Wed Sep 12 2018 Vaughan <devel at agrez dot net> - 20180912-1.70c60c5
- Sync to latest git commit: 70c60c5c57d9d639fbd92276f18558ada51b7c53

* Mon Aug 27 2018 Vaughan <devel at agrez dot net> - 20180827-1.200c2f4
- Sync to latest git commit: 200c2f4dd54b2048b5dcb8661ea3f232beb7d81e

* Sat Aug 18 2018 Vaughan <devel at agrez dot net> - 20180818-1.ebbecf9
- Sync to latest git commit: ebbecf992a466f9bffbd9e3f443f56f64994a277

* Tue Jul 31 2018 Vaughan <devel at agrez dot net> - 20180731-1.83146e2
- Sync to latest git commit: 83146e2ec7fec863fdd6dcaa1b5129c43a5b3699

* Thu Jul 19 2018 Vaughan <devel at agrez dot net> - 20180719-1.bffe7ee
- Sync to latest git commit: bffe7ee6b276f23822883f3d7fd7b705d12c26b9

* Sun Jun 17 2018 Vaughan <devel at agrez dot net> - 20180617-1.adcd4a2
- Sync to latest git commit: adcd4a2e072af5c6f5f09e2d361fd814bc2747c2

* Thu May 31 2018 Vaughan <devel at agrez dot net> - 20180531-1.784fe6c
- Sync to latest git commit: 784fe6cebd9e5726c0c7b9e449f7cdbf2cf6959d

* Mon May 21 2018 Vaughan <devel at agrez dot net> - 20180521-1.a46b1f9
- Sync to latest git commit: a46b1f9521229ec26a1377aab7d013df1ade2791

* Fri May 11 2018 Vaughan <devel at agrez dot net> - 20180511-1.54d8888
- Sync to latest git commit: 54d8888d5b8048af9f7765cfd632faff78ac8053

* Mon Apr 30 2018 Vaughan <devel at agrez dot net> - 20180430-1.983b091
- Sync to latest git commit: 983b091aa491dc6b47e5cc62abb281dbcb75088d

* Wed Apr 18 2018 Vaughan <devel at agrez dot net> - 20180418-1.a154f21
- Sync to latest git commit: a154f2136850dba827cf4bc40794854376902cbd

* Sun Apr 08 2018 Vaughan <devel at agrez dot net> - 20180408-1.3aa8060
- Sync to latest git commit: 3aa806091dc57b757790b026c01754883cee2abc

* Sun Apr 01 2018 Vaughan <devel at agrez dot net> - 20180401-1.c14a903
- Sync to latest git commit: c14a90333c13f507ab219d583b74a998ec11a6e7

* Sun Mar 18 2018 Vaughan <devel at agrez dot net> - 20180318-1.25cf637
- Sync to latest git commit: 25cf637ccc90d7d2fa37277c807ab33b655bd0f4

* Sat Feb 10 2018 Vaughan <devel at agrez dot net> - 20180210-1.b1a7f4a
- Sync to latest git commit: b1a7f4aea6cbd380319c2849ecc5988f9a4dba70

* Mon Feb 05 2018 Vaughan <devel at agrez dot net> - 20180205-1.5d1eb30
- Sync to latest git commit: 5d1eb304cb6706246e6d44c01c48657e07a53383

* Tue Dec 19 2017 Vaughan <devel at agrez dot net> - 20171219-1.dadde5e
- Sync to latest git commit: dadde5e144f4c8d23f37181f785cc7db134b1c1e

* Wed Nov 22 2017 Vaughan <devel at agrez dot net> - 20171102-1.abfb4be
- Sync to latest git commit: abfb4be3e1b5836e1ffd96de4ce499406ec9dbb8

* Thu Nov 02 2017 Vaughan <devel at agrez dot net> - 20171102-1.d5088b0
- Sync to latest git commit: d5088b03a0185c6c9a60cf0dd0a18f0838c6b18d

* Sun Sep 24 2017 Vaughan <devel at agrez dot net> - 20170924-1.eb04fcf
- Sync to latest git commit: eb04fcf96b9ff37d00919ce4e1999f802ed8976f

* Sat Jul 22 2017 Vaughan <devel at agrez dot net> - 20170722-1.1676ddb
- Sync to latest git commit: 1676ddb0792f1d1678efed0399c55128bc8203a6

* Mon Jun 19 2017 Vaughan <devel at agrez dot net> - 20170619-1.dc069bf
- Sync to latest git commit: dc069bfd18c0134713fb877afe2e3442fec27966

* Thu Jun 01 2017 Vaughan <devel at agrez dot net> - 20170601-1.0f315f8
- Sync to latest git commit: 0f315f88ac91f9be93544bfd757f8d55ca4cf099

* Tue May 09 2017 Vaughan <devel at agrez dot net> - 20170509-1.f924320
- Sync to latest git commit: f924320b83f29ee3110876f51929279d9a5b800a

* Tue Mar 14 2017 Vaughan <devel at agrez dot net> - 20170314-1.509beaa
- Sync to latest git commit: 509beaab0e102cf6decf209922669700c9ac5576

* Fri Feb 10 2017 Vaughan <devel at agrez dot net> - 20170210-1.db5fd5e
- Sync to latest git commit: db5fd5e3bbdd3af148696661877f932c2e2415cd

* Sun Feb 05 2017 Vaughan <devel at agrez dot net> - 20170205-1.72b44d8
- Sync to latest git commit: 72b44d850dc8c2307cf0dccea00928702e16bc12

* Sun Jan 15 2017 Vaughan <devel at agrez dot net> - 20170115-1.3c3ff70
- Sync to latest git commit: 3c3ff70bf9f8c0c8e4bc3fd7b5d08df53233ad4d

* Mon Jan 02 2017 Vaughan <devel at agrez dot net> - 20170102-1.4aac0c5
- Sync to latest git commit: 4aac0c5507a7ce8916087060809b3308dae8f731

* Sun Dec 18 2016 Vaughan <devel at agrez dot net> - 20161218-1.2190eba
- Sync to latest git commit: 2190ebaaab17d690fb4a6aa767ff7755eaf51b12
- Use %{sources} macro in %%prep

* Wed Oct 12 2016 Vaughan <devel at agrez dot net> - 20161012-1.a021d6e
- Sync to latest git commit: a021d6e70bf5a710c364d21852be4a8dd4dc423a

* Wed Oct 05 2016 Vaughan <devel at agrez dot net> - 20161005-1.ec63df1
- Sync to latest git commit: ec63df146f454e8cab7080380f9138246d877013

* Thu Sep 15 2016 Vaughan <devel at agrez dot net> - 20160915-1.83dc067
- Sync to latest git commit: 83dc067c60fd3f66eda1114eab23e45f57be387d
- %%license COPYING.linux

* Mon Aug 15 2016 Vaughan <devel at agrez dot net> - 20160815-1.2cf8fd5
- Sync to latest git commit: 2cf8fd5ba0b195e16627df6a5b45f47c0edc3a54

* Thu Jun 16 2016 Vaughan <devel at agrez dot net> - 20160616-1.fdbca29
- Sync to latest git commit: fdbca29d3863ee16f5eee24c66e826bedf662db5

* Sat Jun 04 2016 Vaughan <devel at agrez dot net> - 20160604-1.70143fe
- Sync to latest git commit: 70143fe9d371cd6486a80d6765e93b5574212b64

* Tue May 24 2016 Vaughan <devel at agrez dot net> - 20160524-1.3b98f74
- Sync to latest git commit: 3b98f7433649e13cf08f54f509d11491c99c4c0b

* Wed Apr 27 2016 Vaughan <devel at agrez dot net> - 20160427-1.20958cd
- Sync to latest git commit: 20958cdfe145aacdc64bded239c9d7bfe1b20bb2

* Sat Mar 19 2016 Vaughan <devel at agrez dot net> - 20160311-1.c230b2b
- Sync to latest git commit: c230b2b9b5a38615a4ab17539c3b438064fe5d83

* Fri Mar 11 2016 Vaughan <devel at agrez dot net> - 20160311-1.8b4e548
- Sync to latest git commit: 8b4e5482b52e6fb438dddc0d88ba0ba8d44af54b

* Mon Mar 07 2016 Vaughan <devel at agrez dot net> - 20160307-1.cb2ffaa
- Don't grab a whole repo snapshot as Source0 is too big (~110 MB).
- Only add the required firmware files / docs as Sources(0-9)
- Drop README file (its provided by the kernel)

* Mon Mar 07 2016 mrjoshuap <jpreston at redhat dot com> - 20160305-1.845eb06
- Sync to latest git commit: 845eb064cb52af00f2ea33c0c9c54136f664a3e4

* Fri Feb 05 2016 Vaughan <devel at agrez dot net> - 20160205-1.cb2ffaa
- Sync to latest git commit: cb2ffaa5503ac53039d40715965480dd66f0aa20

* Wed Dec 23 2015 Vaughan <devel at agrez dot net> - 20151223-1.1efc1ec
- Sync to latest git commit: 1efc1ece0d1e282b1cf4f371d2f7c4098113c098

* Sat Dec 12 2015 Vaughan <devel at agrez dot net> - 20151212-1.36c56b7
- Sync to latest git commit: 36c56b7cab316e657bc00392fd98ceded38a17ae

* Sun Nov 29 2015 Vaughan <devel at agrez dot net> - 20151125-1.f01ec42
- Sync to latest git commit: f01ec42f66e360a177f82457e3324adbfdf84de5

* Sun Nov 15 2015 Vaughan <devel at agrez dot net> - 20151114-1.fa62739
- Sync to latest git commit: fa627390f76d7d3c38e80fc88ad1cc6697c04334

* Thu Oct 29 2015 Vaughan <devel at agrez dot net> - 20151013-1.4047fe2
- Sync to latest git commit: 4047fe26797884cedf53bc8671d19e7f6f9f59d5

* Tue Oct 13 2015 Vaughan <devel at agrez dot net> - 20151013-1.ba7a8fb
- Sync to latest git revision:
  git commit: ba7a8fb709adab287495f4e836b1cd3e5c9db409

* Thu Sep 24 2015 Vaughan <devel at agrez dot net> - 20150924-1.960832a
- Sync to latest git revision:
  git commit: 960832a6c2590635216c296b6ee0bebf67b21d50

* Thu Sep 17 2015 Vaughan <devel at agrez dot net> - 20150916-1.56d5a7b
- Sync to latest git revision:
  git commit: 56d5a7bca477e0297d94aace43320c38df985015

* Fri Sep 11 2015 Vaughan <devel at agrez dot net> - 20150911-1.fc95251
- Sync to latest git revision:
  git commit: fc952516e1d73d54141861a64ac5d4be17e7a159

* Wed Sep 02 2015 Vaughan <devel at agrez dot net> - 20150902-1.c6ae1d6
- Sync to latest git revision:
  git commit: c6ae1d69860c0915cca303475abc0b4efb83ad08

* Wed Aug 19 2015 Vaughan <devel at agrez dot net> - 20150819-1.b3da683
- Sync to latest git revision:
  git commit: b3da68379785b0e10b09fdaa8db1b6f18732be8e

* Sat Aug 15 2015 Vaughan <devel at agrez dot net> - 20150815-1.c25cc51
- Sync to latest git revision:
  git commit: c25cc51c6fc0ddc4455d56ad26fbbf38b48da33a

* Sat Aug 08 2015 Vaughan <devel at agrez dot net> - 20150808-1.11eaffc
- Update for kernel 4.1.y
  git commit: 11eaffc2bbb61c6911ffa05b80694f9f7d91915c

* Sat Jul 25 2015 Vaughan <devel at agrez dot net> - 20150725-1.464ce4f
- Update for kernel 4.0.9
  git commit: 464ce4fc013ff20a2b957bc47093ed8b557e1ef1

* Sat Jun 27 2015 Vaughan <devel at agrez dot net> - 20150624-1.856e2e1
- Update for kernel 4.0.6
  git commit: 856e2e1907a7f7058289c30268515c8cbf3fa5e3

* Sat Jun 20 2015 Vaughan <devel at agrez dot net> - 20150620-1.8b9d7b8
- Initial build
