# This file was automatically created by FeynRules 2.3.32
# Mathematica version: 11.3.0 for Linux x86 (64-bit) (March 7, 2018)
# Date: Mon 25 Feb 2019 18:52:00


from object_library import all_decays, Decay
import particles as P


Decay_b = Decay(name = 'Decay_b',
                particle = P.b,
                partial_widths = {(P.W__minus__,P.c):'(((3*CKM2x3*ee**2*MB**2*complexconjugate(CKM2x3))/(2.*sw**2) + (3*CKM2x3*ee**2*MC**2*complexconjugate(CKM2x3))/(2.*sw**2) + (3*CKM2x3*ee**2*MB**4*complexconjugate(CKM2x3))/(2.*MW**2*sw**2) - (3*CKM2x3*ee**2*MB**2*MC**2*complexconjugate(CKM2x3))/(MW**2*sw**2) + (3*CKM2x3*ee**2*MC**4*complexconjugate(CKM2x3))/(2.*MW**2*sw**2) - (3*CKM2x3*ee**2*MW**2*complexconjugate(CKM2x3))/sw**2)*cmath.sqrt(MB**4 - 2*MB**2*MC**2 + MC**4 - 2*MB**2*MW**2 - 2*MC**2*MW**2 + MW**4))/(96.*cmath.pi*abs(MB)**3)',
                                  (P.W__minus__,P.t):'(((3*CKM3x3*ee**2*MB**2*complexconjugate(CKM3x3))/(2.*sw**2) + (3*CKM3x3*ee**2*MT**2*complexconjugate(CKM3x3))/(2.*sw**2) + (3*CKM3x3*ee**2*MB**4*complexconjugate(CKM3x3))/(2.*MW**2*sw**2) - (3*CKM3x3*ee**2*MB**2*MT**2*complexconjugate(CKM3x3))/(MW**2*sw**2) + (3*CKM3x3*ee**2*MT**4*complexconjugate(CKM3x3))/(2.*MW**2*sw**2) - (3*CKM3x3*ee**2*MW**2*complexconjugate(CKM3x3))/sw**2)*cmath.sqrt(MB**4 - 2*MB**2*MT**2 + MT**4 - 2*MB**2*MW**2 - 2*MT**2*MW**2 + MW**4))/(96.*cmath.pi*abs(MB)**3)',
                                  (P.W__minus__,P.u):'(((3*CKM1x3*ee**2*MB**2*complexconjugate(CKM1x3))/(2.*sw**2) + (3*CKM1x3*ee**2*MU**2*complexconjugate(CKM1x3))/(2.*sw**2) + (3*CKM1x3*ee**2*MB**4*complexconjugate(CKM1x3))/(2.*MW**2*sw**2) - (3*CKM1x3*ee**2*MB**2*MU**2*complexconjugate(CKM1x3))/(MW**2*sw**2) + (3*CKM1x3*ee**2*MU**4*complexconjugate(CKM1x3))/(2.*MW**2*sw**2) - (3*CKM1x3*ee**2*MW**2*complexconjugate(CKM1x3))/sw**2)*cmath.sqrt(MB**4 - 2*MB**2*MU**2 + MU**4 - 2*MB**2*MW**2 - 2*MU**2*MW**2 + MW**4))/(96.*cmath.pi*abs(MB)**3)'})

Decay_c = Decay(name = 'Decay_c',
                particle = P.c,
                partial_widths = {(P.W__plus__,P.b):'(((3*CKM2x3*ee**2*MB**2*complexconjugate(CKM2x3))/(2.*sw**2) + (3*CKM2x3*ee**2*MC**2*complexconjugate(CKM2x3))/(2.*sw**2) + (3*CKM2x3*ee**2*MB**4*complexconjugate(CKM2x3))/(2.*MW**2*sw**2) - (3*CKM2x3*ee**2*MB**2*MC**2*complexconjugate(CKM2x3))/(MW**2*sw**2) + (3*CKM2x3*ee**2*MC**4*complexconjugate(CKM2x3))/(2.*MW**2*sw**2) - (3*CKM2x3*ee**2*MW**2*complexconjugate(CKM2x3))/sw**2)*cmath.sqrt(MB**4 - 2*MB**2*MC**2 + MC**4 - 2*MB**2*MW**2 - 2*MC**2*MW**2 + MW**4))/(96.*cmath.pi*abs(MC)**3)',
                                  (P.W__plus__,P.d):'(((3*CKM2x1*ee**2*MC**2*complexconjugate(CKM2x1))/(2.*sw**2) + (3*CKM2x1*ee**2*MD**2*complexconjugate(CKM2x1))/(2.*sw**2) + (3*CKM2x1*ee**2*MC**4*complexconjugate(CKM2x1))/(2.*MW**2*sw**2) - (3*CKM2x1*ee**2*MC**2*MD**2*complexconjugate(CKM2x1))/(MW**2*sw**2) + (3*CKM2x1*ee**2*MD**4*complexconjugate(CKM2x1))/(2.*MW**2*sw**2) - (3*CKM2x1*ee**2*MW**2*complexconjugate(CKM2x1))/sw**2)*cmath.sqrt(MC**4 - 2*MC**2*MD**2 + MD**4 - 2*MC**2*MW**2 - 2*MD**2*MW**2 + MW**4))/(96.*cmath.pi*abs(MC)**3)',
                                  (P.W__plus__,P.s):'(((3*CKM2x2*ee**2*MC**2*complexconjugate(CKM2x2))/(2.*sw**2) + (3*CKM2x2*ee**2*MS**2*complexconjugate(CKM2x2))/(2.*sw**2) + (3*CKM2x2*ee**2*MC**4*complexconjugate(CKM2x2))/(2.*MW**2*sw**2) - (3*CKM2x2*ee**2*MC**2*MS**2*complexconjugate(CKM2x2))/(MW**2*sw**2) + (3*CKM2x2*ee**2*MS**4*complexconjugate(CKM2x2))/(2.*MW**2*sw**2) - (3*CKM2x2*ee**2*MW**2*complexconjugate(CKM2x2))/sw**2)*cmath.sqrt(MC**4 - 2*MC**2*MS**2 + MS**4 - 2*MC**2*MW**2 - 2*MS**2*MW**2 + MW**4))/(96.*cmath.pi*abs(MC)**3)'})

Decay_P__tilde__Chi__plus__ = Decay(name = 'Decay_P__tilde__Chi__plus__',
                                    particle = P.P__tilde__Chi__plus__,
                                    partial_widths = {(P.phi__plus__,P.P__tilde__Psi):'((2*MChi**2*yl1**2 - 2*Mphi**2*yl1**2 + 4*MChi*MPsi*yl1**2 + 2*MPsi**2*yl1**2)*cmath.sqrt(MChi**4 - 2*MChi**2*Mphi**2 + Mphi**4 - 2*MChi**2*MPsi**2 - 2*Mphi**2*MPsi**2 + MPsi**4))/(32.*cmath.pi*abs(MChi)**3)'})

Decay_d = Decay(name = 'Decay_d',
                particle = P.d,
                partial_widths = {(P.W__minus__,P.c):'(((3*CKM2x1*ee**2*MC**2*complexconjugate(CKM2x1))/(2.*sw**2) + (3*CKM2x1*ee**2*MD**2*complexconjugate(CKM2x1))/(2.*sw**2) + (3*CKM2x1*ee**2*MC**4*complexconjugate(CKM2x1))/(2.*MW**2*sw**2) - (3*CKM2x1*ee**2*MC**2*MD**2*complexconjugate(CKM2x1))/(MW**2*sw**2) + (3*CKM2x1*ee**2*MD**4*complexconjugate(CKM2x1))/(2.*MW**2*sw**2) - (3*CKM2x1*ee**2*MW**2*complexconjugate(CKM2x1))/sw**2)*cmath.sqrt(MC**4 - 2*MC**2*MD**2 + MD**4 - 2*MC**2*MW**2 - 2*MD**2*MW**2 + MW**4))/(96.*cmath.pi*abs(MD)**3)',
                                  (P.W__minus__,P.t):'(((3*CKM3x1*ee**2*MD**2*complexconjugate(CKM3x1))/(2.*sw**2) + (3*CKM3x1*ee**2*MT**2*complexconjugate(CKM3x1))/(2.*sw**2) + (3*CKM3x1*ee**2*MD**4*complexconjugate(CKM3x1))/(2.*MW**2*sw**2) - (3*CKM3x1*ee**2*MD**2*MT**2*complexconjugate(CKM3x1))/(MW**2*sw**2) + (3*CKM3x1*ee**2*MT**4*complexconjugate(CKM3x1))/(2.*MW**2*sw**2) - (3*CKM3x1*ee**2*MW**2*complexconjugate(CKM3x1))/sw**2)*cmath.sqrt(MD**4 - 2*MD**2*MT**2 + MT**4 - 2*MD**2*MW**2 - 2*MT**2*MW**2 + MW**4))/(96.*cmath.pi*abs(MD)**3)',
                                  (P.W__minus__,P.u):'(((3*CKM1x1*ee**2*MD**2*complexconjugate(CKM1x1))/(2.*sw**2) + (3*CKM1x1*ee**2*MU**2*complexconjugate(CKM1x1))/(2.*sw**2) + (3*CKM1x1*ee**2*MD**4*complexconjugate(CKM1x1))/(2.*MW**2*sw**2) - (3*CKM1x1*ee**2*MD**2*MU**2*complexconjugate(CKM1x1))/(MW**2*sw**2) + (3*CKM1x1*ee**2*MU**4*complexconjugate(CKM1x1))/(2.*MW**2*sw**2) - (3*CKM1x1*ee**2*MW**2*complexconjugate(CKM1x1))/sw**2)*cmath.sqrt(MD**4 - 2*MD**2*MU**2 + MU**4 - 2*MD**2*MW**2 - 2*MU**2*MW**2 + MW**4))/(96.*cmath.pi*abs(MD)**3)'})

Decay_e__minus__ = Decay(name = 'Decay_e__minus__',
                         particle = P.e__minus__,
                         partial_widths = {(P.phi__minus__,P.NN1):'((Me**2*y2e**2 + MNN1**2*y2e**2 - Mphi**2*y2e**2)*cmath.sqrt(Me**4 - 2*Me**2*MNN1**2 + MNN1**4 - 2*Me**2*Mphi**2 - 2*MNN1**2*Mphi**2 + Mphi**4))/(32.*cmath.pi*abs(Me)**3)',
                                           (P.W__minus__,P.ve):'((Me**2 - MW**2)*((ee**2*Me**2)/(2.*sw**2) + (ee**2*Me**4)/(2.*MW**2*sw**2) - (ee**2*MW**2)/sw**2))/(32.*cmath.pi*abs(Me)**3)'})

Decay_H = Decay(name = 'Decay_H',
                particle = P.H,
                partial_widths = {(P.b,P.b__tilde__):'((-12*MB**2*yb**2 + 3*MH**2*yb**2)*cmath.sqrt(-4*MB**2*MH**2 + MH**4))/(16.*cmath.pi*abs(MH)**3)',
                                  (P.c,P.c__tilde__):'((-12*MC**2*yc**2 + 3*MH**2*yc**2)*cmath.sqrt(-4*MC**2*MH**2 + MH**4))/(16.*cmath.pi*abs(MH)**3)',
                                  (P.d,P.d__tilde__):'((-12*MD**2*ydo**2 + 3*MH**2*ydo**2)*cmath.sqrt(-4*MD**2*MH**2 + MH**4))/(16.*cmath.pi*abs(MH)**3)',
                                  (P.e__minus__,P.e__plus__):'((-4*Me**2*ye**2 + MH**2*ye**2)*cmath.sqrt(-4*Me**2*MH**2 + MH**4))/(16.*cmath.pi*abs(MH)**3)',
                                  (P.mu__minus__,P.mu__plus__):'((MH**2*ym**2 - 4*MMU**2*ym**2)*cmath.sqrt(MH**4 - 4*MH**2*MMU**2))/(16.*cmath.pi*abs(MH)**3)',
                                  (P.NN1,P.ve__tilde__):'((MH**2 - MNN1**2)*((MH**2*yNe**2)/2. - (MNN1**2*yNe**2)/2.))/(16.*cmath.pi*abs(MH)**3)',
                                  (P.NN2,P.vm__tilde__):'((MH**2 - MNN2**2)*((MH**2*yNm**2)/2. - (MNN2**2*yNm**2)/2.))/(16.*cmath.pi*abs(MH)**3)',
                                  (P.NN3,P.vt__tilde__):'((MH**2 - MNN3**2)*((MH**2*yNt**2)/2. - (MNN3**2*yNt**2)/2.))/(16.*cmath.pi*abs(MH)**3)',
                                  (P.phi__minus__,P.phi__plus__):'(lam1**2*vev**2*cmath.sqrt(MH**4 - 4*MH**2*Mphi**2))/(16.*cmath.pi*abs(MH)**3)',
                                  (P.s,P.s__tilde__):'((3*MH**2*ys**2 - 12*MS**2*ys**2)*cmath.sqrt(MH**4 - 4*MH**2*MS**2))/(16.*cmath.pi*abs(MH)**3)',
                                  (P.t,P.t__tilde__):'((3*MH**2*yt**2 - 12*MT**2*yt**2)*cmath.sqrt(MH**4 - 4*MH**2*MT**2))/(16.*cmath.pi*abs(MH)**3)',
                                  (P.ta__minus__,P.ta__plus__):'((MH**2*ytau**2 - 4*MTA**2*ytau**2)*cmath.sqrt(MH**4 - 4*MH**2*MTA**2))/(16.*cmath.pi*abs(MH)**3)',
                                  (P.u,P.u__tilde__):'((3*MH**2*yup**2 - 12*MU**2*yup**2)*cmath.sqrt(MH**4 - 4*MH**2*MU**2))/(16.*cmath.pi*abs(MH)**3)',
                                  (P.ve,P.NN1__tilde__):'((MH**2 - MNN1**2)*((MH**2*yNe**2)/2. - (MNN1**2*yNe**2)/2.))/(16.*cmath.pi*abs(MH)**3)',
                                  (P.vm,P.NN2__tilde__):'((MH**2 - MNN2**2)*((MH**2*yNm**2)/2. - (MNN2**2*yNm**2)/2.))/(16.*cmath.pi*abs(MH)**3)',
                                  (P.vt,P.NN3__tilde__):'((MH**2 - MNN3**2)*((MH**2*yNt**2)/2. - (MNN3**2*yNt**2)/2.))/(16.*cmath.pi*abs(MH)**3)',
                                  (P.W__minus__,P.W__plus__):'(((3*ee**4*vev**2)/(4.*sw**4) + (ee**4*MH**4*vev**2)/(16.*MW**4*sw**4) - (ee**4*MH**2*vev**2)/(4.*MW**2*sw**4))*cmath.sqrt(MH**4 - 4*MH**2*MW**2))/(16.*cmath.pi*abs(MH)**3)',
                                  (P.Z,P.Z):'(((9*ee**4*vev**2)/2. + (3*ee**4*MH**4*vev**2)/(8.*MZ**4) - (3*ee**4*MH**2*vev**2)/(2.*MZ**2) + (3*cw**4*ee**4*vev**2)/(4.*sw**4) + (cw**4*ee**4*MH**4*vev**2)/(16.*MZ**4*sw**4) - (cw**4*ee**4*MH**2*vev**2)/(4.*MZ**2*sw**4) + (3*cw**2*ee**4*vev**2)/sw**2 + (cw**2*ee**4*MH**4*vev**2)/(4.*MZ**4*sw**2) - (cw**2*ee**4*MH**2*vev**2)/(MZ**2*sw**2) + (3*ee**4*sw**2*vev**2)/cw**2 + (ee**4*MH**4*sw**2*vev**2)/(4.*cw**2*MZ**4) - (ee**4*MH**2*sw**2*vev**2)/(cw**2*MZ**2) + (3*ee**4*sw**4*vev**2)/(4.*cw**4) + (ee**4*MH**4*sw**4*vev**2)/(16.*cw**4*MZ**4) - (ee**4*MH**2*sw**4*vev**2)/(4.*cw**4*MZ**2))*cmath.sqrt(MH**4 - 4*MH**2*MZ**2))/(32.*cmath.pi*abs(MH)**3)'})

Decay_mu__minus__ = Decay(name = 'Decay_mu__minus__',
                          particle = P.mu__minus__,
                          partial_widths = {(P.phi__minus__,P.NN2):'((MMU**2*y2m**2 + MNN2**2*y2m**2 - Mphi**2*y2m**2)*cmath.sqrt(MMU**4 - 2*MMU**2*MNN2**2 + MNN2**4 - 2*MMU**2*Mphi**2 - 2*MNN2**2*Mphi**2 + Mphi**4))/(32.*cmath.pi*abs(MMU)**3)',
                                            (P.W__minus__,P.vm):'((MMU**2 - MW**2)*((ee**2*MMU**2)/(2.*sw**2) + (ee**2*MMU**4)/(2.*MW**2*sw**2) - (ee**2*MW**2)/sw**2))/(32.*cmath.pi*abs(MMU)**3)'})

Decay_NN1 = Decay(name = 'Decay_NN1',
                  particle = P.NN1,
                  partial_widths = {(P.H,P.ve):'((-MH**2 + MNN1**2)*(-(MH**2*yNe**2)/2. + (MNN1**2*yNe**2)/2.))/(32.*cmath.pi*abs(MNN1)**3)',
                                    (P.phi__plus__,P.e__minus__):'((Me**2*y2e**2 + MNN1**2*y2e**2 - Mphi**2*y2e**2)*cmath.sqrt(Me**4 - 2*Me**2*MNN1**2 + MNN1**4 - 2*Me**2*Mphi**2 - 2*MNN1**2*Mphi**2 + Mphi**4))/(32.*cmath.pi*abs(MNN1)**3)'})

Decay_NN2 = Decay(name = 'Decay_NN2',
                  particle = P.NN2,
                  partial_widths = {(P.H,P.vm):'((-MH**2 + MNN2**2)*(-(MH**2*yNm**2)/2. + (MNN2**2*yNm**2)/2.))/(32.*cmath.pi*abs(MNN2)**3)',
                                    (P.phi__plus__,P.mu__minus__):'((MMU**2*y2m**2 + MNN2**2*y2m**2 - Mphi**2*y2m**2)*cmath.sqrt(MMU**4 - 2*MMU**2*MNN2**2 + MNN2**4 - 2*MMU**2*Mphi**2 - 2*MNN2**2*Mphi**2 + Mphi**4))/(32.*cmath.pi*abs(MNN2)**3)'})

Decay_NN3 = Decay(name = 'Decay_NN3',
                  particle = P.NN3,
                  partial_widths = {(P.H,P.vt):'((-MH**2 + MNN3**2)*(-(MH**2*yNt**2)/2. + (MNN3**2*yNt**2)/2.))/(32.*cmath.pi*abs(MNN3)**3)',
                                    (P.phi__plus__,P.ta__minus__):'((MNN3**2*y2t**2 - Mphi**2*y2t**2 + MTA**2*y2t**2)*cmath.sqrt(MNN3**4 - 2*MNN3**2*Mphi**2 + Mphi**4 - 2*MNN3**2*MTA**2 - 2*Mphi**2*MTA**2 + MTA**4))/(32.*cmath.pi*abs(MNN3)**3)'})

Decay_phi__plus__ = Decay(name = 'Decay_phi__plus__',
                          particle = P.phi__plus__,
                          partial_widths = {(P.P__tilde__Chi__plus__,P.P__tilde__Psi__tilde__):'((-2*MChi**2*yl1**2 + 2*Mphi**2*yl1**2 - 4*MChi*MPsi*yl1**2 - 2*MPsi**2*yl1**2)*cmath.sqrt(MChi**4 - 2*MChi**2*Mphi**2 + Mphi**4 - 2*MChi**2*MPsi**2 - 2*Mphi**2*MPsi**2 + MPsi**4))/(16.*cmath.pi*abs(Mphi)**3)',
                                            (P.NN1,P.e__plus__):'((-(Me**2*y2e**2) - MNN1**2*y2e**2 + Mphi**2*y2e**2)*cmath.sqrt(Me**4 - 2*Me**2*MNN1**2 + MNN1**4 - 2*Me**2*Mphi**2 - 2*MNN1**2*Mphi**2 + Mphi**4))/(16.*cmath.pi*abs(Mphi)**3)',
                                            (P.NN2,P.mu__plus__):'((-(MMU**2*y2m**2) - MNN2**2*y2m**2 + Mphi**2*y2m**2)*cmath.sqrt(MMU**4 - 2*MMU**2*MNN2**2 + MNN2**4 - 2*MMU**2*Mphi**2 - 2*MNN2**2*Mphi**2 + Mphi**4))/(16.*cmath.pi*abs(Mphi)**3)',
                                            (P.NN3,P.ta__plus__):'((-(MNN3**2*y2t**2) + Mphi**2*y2t**2 - MTA**2*y2t**2)*cmath.sqrt(MNN3**4 - 2*MNN3**2*Mphi**2 + Mphi**4 - 2*MNN3**2*MTA**2 - 2*Mphi**2*MTA**2 + MTA**4))/(16.*cmath.pi*abs(Mphi)**3)'})

Decay_P__tilde__Psi = Decay(name = 'Decay_P__tilde__Psi',
                            particle = P.P__tilde__Psi,
                            partial_widths = {(P.phi__minus__,P.P__tilde__Chi__plus__):'((2*MChi**2*yl1**2 - 2*Mphi**2*yl1**2 + 4*MChi*MPsi*yl1**2 + 2*MPsi**2*yl1**2)*cmath.sqrt(MChi**4 - 2*MChi**2*Mphi**2 + Mphi**4 - 2*MChi**2*MPsi**2 - 2*Mphi**2*MPsi**2 + MPsi**4))/(32.*cmath.pi*abs(MPsi)**3)'})

Decay_s = Decay(name = 'Decay_s',
                particle = P.s,
                partial_widths = {(P.W__minus__,P.c):'(((3*CKM2x2*ee**2*MC**2*complexconjugate(CKM2x2))/(2.*sw**2) + (3*CKM2x2*ee**2*MS**2*complexconjugate(CKM2x2))/(2.*sw**2) + (3*CKM2x2*ee**2*MC**4*complexconjugate(CKM2x2))/(2.*MW**2*sw**2) - (3*CKM2x2*ee**2*MC**2*MS**2*complexconjugate(CKM2x2))/(MW**2*sw**2) + (3*CKM2x2*ee**2*MS**4*complexconjugate(CKM2x2))/(2.*MW**2*sw**2) - (3*CKM2x2*ee**2*MW**2*complexconjugate(CKM2x2))/sw**2)*cmath.sqrt(MC**4 - 2*MC**2*MS**2 + MS**4 - 2*MC**2*MW**2 - 2*MS**2*MW**2 + MW**4))/(96.*cmath.pi*abs(MS)**3)',
                                  (P.W__minus__,P.t):'(((3*CKM3x2*ee**2*MS**2*complexconjugate(CKM3x2))/(2.*sw**2) + (3*CKM3x2*ee**2*MT**2*complexconjugate(CKM3x2))/(2.*sw**2) + (3*CKM3x2*ee**2*MS**4*complexconjugate(CKM3x2))/(2.*MW**2*sw**2) - (3*CKM3x2*ee**2*MS**2*MT**2*complexconjugate(CKM3x2))/(MW**2*sw**2) + (3*CKM3x2*ee**2*MT**4*complexconjugate(CKM3x2))/(2.*MW**2*sw**2) - (3*CKM3x2*ee**2*MW**2*complexconjugate(CKM3x2))/sw**2)*cmath.sqrt(MS**4 - 2*MS**2*MT**2 + MT**4 - 2*MS**2*MW**2 - 2*MT**2*MW**2 + MW**4))/(96.*cmath.pi*abs(MS)**3)',
                                  (P.W__minus__,P.u):'(((3*CKM1x2*ee**2*MS**2*complexconjugate(CKM1x2))/(2.*sw**2) + (3*CKM1x2*ee**2*MU**2*complexconjugate(CKM1x2))/(2.*sw**2) + (3*CKM1x2*ee**2*MS**4*complexconjugate(CKM1x2))/(2.*MW**2*sw**2) - (3*CKM1x2*ee**2*MS**2*MU**2*complexconjugate(CKM1x2))/(MW**2*sw**2) + (3*CKM1x2*ee**2*MU**4*complexconjugate(CKM1x2))/(2.*MW**2*sw**2) - (3*CKM1x2*ee**2*MW**2*complexconjugate(CKM1x2))/sw**2)*cmath.sqrt(MS**4 - 2*MS**2*MU**2 + MU**4 - 2*MS**2*MW**2 - 2*MU**2*MW**2 + MW**4))/(96.*cmath.pi*abs(MS)**3)'})

Decay_t = Decay(name = 'Decay_t',
                particle = P.t,
                partial_widths = {(P.W__plus__,P.b):'(((3*CKM3x3*ee**2*MB**2*complexconjugate(CKM3x3))/(2.*sw**2) + (3*CKM3x3*ee**2*MT**2*complexconjugate(CKM3x3))/(2.*sw**2) + (3*CKM3x3*ee**2*MB**4*complexconjugate(CKM3x3))/(2.*MW**2*sw**2) - (3*CKM3x3*ee**2*MB**2*MT**2*complexconjugate(CKM3x3))/(MW**2*sw**2) + (3*CKM3x3*ee**2*MT**4*complexconjugate(CKM3x3))/(2.*MW**2*sw**2) - (3*CKM3x3*ee**2*MW**2*complexconjugate(CKM3x3))/sw**2)*cmath.sqrt(MB**4 - 2*MB**2*MT**2 + MT**4 - 2*MB**2*MW**2 - 2*MT**2*MW**2 + MW**4))/(96.*cmath.pi*abs(MT)**3)',
                                  (P.W__plus__,P.d):'(((3*CKM3x1*ee**2*MD**2*complexconjugate(CKM3x1))/(2.*sw**2) + (3*CKM3x1*ee**2*MT**2*complexconjugate(CKM3x1))/(2.*sw**2) + (3*CKM3x1*ee**2*MD**4*complexconjugate(CKM3x1))/(2.*MW**2*sw**2) - (3*CKM3x1*ee**2*MD**2*MT**2*complexconjugate(CKM3x1))/(MW**2*sw**2) + (3*CKM3x1*ee**2*MT**4*complexconjugate(CKM3x1))/(2.*MW**2*sw**2) - (3*CKM3x1*ee**2*MW**2*complexconjugate(CKM3x1))/sw**2)*cmath.sqrt(MD**4 - 2*MD**2*MT**2 + MT**4 - 2*MD**2*MW**2 - 2*MT**2*MW**2 + MW**4))/(96.*cmath.pi*abs(MT)**3)',
                                  (P.W__plus__,P.s):'(((3*CKM3x2*ee**2*MS**2*complexconjugate(CKM3x2))/(2.*sw**2) + (3*CKM3x2*ee**2*MT**2*complexconjugate(CKM3x2))/(2.*sw**2) + (3*CKM3x2*ee**2*MS**4*complexconjugate(CKM3x2))/(2.*MW**2*sw**2) - (3*CKM3x2*ee**2*MS**2*MT**2*complexconjugate(CKM3x2))/(MW**2*sw**2) + (3*CKM3x2*ee**2*MT**4*complexconjugate(CKM3x2))/(2.*MW**2*sw**2) - (3*CKM3x2*ee**2*MW**2*complexconjugate(CKM3x2))/sw**2)*cmath.sqrt(MS**4 - 2*MS**2*MT**2 + MT**4 - 2*MS**2*MW**2 - 2*MT**2*MW**2 + MW**4))/(96.*cmath.pi*abs(MT)**3)'})

Decay_ta__minus__ = Decay(name = 'Decay_ta__minus__',
                          particle = P.ta__minus__,
                          partial_widths = {(P.phi__minus__,P.NN3):'((MNN3**2*y2t**2 - Mphi**2*y2t**2 + MTA**2*y2t**2)*cmath.sqrt(MNN3**4 - 2*MNN3**2*Mphi**2 + Mphi**4 - 2*MNN3**2*MTA**2 - 2*Mphi**2*MTA**2 + MTA**4))/(32.*cmath.pi*abs(MTA)**3)',
                                            (P.W__minus__,P.vt):'((MTA**2 - MW**2)*((ee**2*MTA**2)/(2.*sw**2) + (ee**2*MTA**4)/(2.*MW**2*sw**2) - (ee**2*MW**2)/sw**2))/(32.*cmath.pi*abs(MTA)**3)'})

Decay_u = Decay(name = 'Decay_u',
                particle = P.u,
                partial_widths = {(P.W__plus__,P.b):'(((3*CKM1x3*ee**2*MB**2*complexconjugate(CKM1x3))/(2.*sw**2) + (3*CKM1x3*ee**2*MU**2*complexconjugate(CKM1x3))/(2.*sw**2) + (3*CKM1x3*ee**2*MB**4*complexconjugate(CKM1x3))/(2.*MW**2*sw**2) - (3*CKM1x3*ee**2*MB**2*MU**2*complexconjugate(CKM1x3))/(MW**2*sw**2) + (3*CKM1x3*ee**2*MU**4*complexconjugate(CKM1x3))/(2.*MW**2*sw**2) - (3*CKM1x3*ee**2*MW**2*complexconjugate(CKM1x3))/sw**2)*cmath.sqrt(MB**4 - 2*MB**2*MU**2 + MU**4 - 2*MB**2*MW**2 - 2*MU**2*MW**2 + MW**4))/(96.*cmath.pi*abs(MU)**3)',
                                  (P.W__plus__,P.d):'(((3*CKM1x1*ee**2*MD**2*complexconjugate(CKM1x1))/(2.*sw**2) + (3*CKM1x1*ee**2*MU**2*complexconjugate(CKM1x1))/(2.*sw**2) + (3*CKM1x1*ee**2*MD**4*complexconjugate(CKM1x1))/(2.*MW**2*sw**2) - (3*CKM1x1*ee**2*MD**2*MU**2*complexconjugate(CKM1x1))/(MW**2*sw**2) + (3*CKM1x1*ee**2*MU**4*complexconjugate(CKM1x1))/(2.*MW**2*sw**2) - (3*CKM1x1*ee**2*MW**2*complexconjugate(CKM1x1))/sw**2)*cmath.sqrt(MD**4 - 2*MD**2*MU**2 + MU**4 - 2*MD**2*MW**2 - 2*MU**2*MW**2 + MW**4))/(96.*cmath.pi*abs(MU)**3)',
                                  (P.W__plus__,P.s):'(((3*CKM1x2*ee**2*MS**2*complexconjugate(CKM1x2))/(2.*sw**2) + (3*CKM1x2*ee**2*MU**2*complexconjugate(CKM1x2))/(2.*sw**2) + (3*CKM1x2*ee**2*MS**4*complexconjugate(CKM1x2))/(2.*MW**2*sw**2) - (3*CKM1x2*ee**2*MS**2*MU**2*complexconjugate(CKM1x2))/(MW**2*sw**2) + (3*CKM1x2*ee**2*MU**4*complexconjugate(CKM1x2))/(2.*MW**2*sw**2) - (3*CKM1x2*ee**2*MW**2*complexconjugate(CKM1x2))/sw**2)*cmath.sqrt(MS**4 - 2*MS**2*MU**2 + MU**4 - 2*MS**2*MW**2 - 2*MU**2*MW**2 + MW**4))/(96.*cmath.pi*abs(MU)**3)'})

Decay_W__plus__ = Decay(name = 'Decay_W__plus__',
                        particle = P.W__plus__,
                        partial_widths = {(P.c,P.b__tilde__):'(((-3*CKM2x3*ee**2*MB**2*complexconjugate(CKM2x3))/(2.*sw**2) - (3*CKM2x3*ee**2*MC**2*complexconjugate(CKM2x3))/(2.*sw**2) - (3*CKM2x3*ee**2*MB**4*complexconjugate(CKM2x3))/(2.*MW**2*sw**2) + (3*CKM2x3*ee**2*MB**2*MC**2*complexconjugate(CKM2x3))/(MW**2*sw**2) - (3*CKM2x3*ee**2*MC**4*complexconjugate(CKM2x3))/(2.*MW**2*sw**2) + (3*CKM2x3*ee**2*MW**2*complexconjugate(CKM2x3))/sw**2)*cmath.sqrt(MB**4 - 2*MB**2*MC**2 + MC**4 - 2*MB**2*MW**2 - 2*MC**2*MW**2 + MW**4))/(48.*cmath.pi*abs(MW)**3)',
                                          (P.c,P.d__tilde__):'(((-3*CKM2x1*ee**2*MC**2*complexconjugate(CKM2x1))/(2.*sw**2) - (3*CKM2x1*ee**2*MD**2*complexconjugate(CKM2x1))/(2.*sw**2) - (3*CKM2x1*ee**2*MC**4*complexconjugate(CKM2x1))/(2.*MW**2*sw**2) + (3*CKM2x1*ee**2*MC**2*MD**2*complexconjugate(CKM2x1))/(MW**2*sw**2) - (3*CKM2x1*ee**2*MD**4*complexconjugate(CKM2x1))/(2.*MW**2*sw**2) + (3*CKM2x1*ee**2*MW**2*complexconjugate(CKM2x1))/sw**2)*cmath.sqrt(MC**4 - 2*MC**2*MD**2 + MD**4 - 2*MC**2*MW**2 - 2*MD**2*MW**2 + MW**4))/(48.*cmath.pi*abs(MW)**3)',
                                          (P.c,P.s__tilde__):'(((-3*CKM2x2*ee**2*MC**2*complexconjugate(CKM2x2))/(2.*sw**2) - (3*CKM2x2*ee**2*MS**2*complexconjugate(CKM2x2))/(2.*sw**2) - (3*CKM2x2*ee**2*MC**4*complexconjugate(CKM2x2))/(2.*MW**2*sw**2) + (3*CKM2x2*ee**2*MC**2*MS**2*complexconjugate(CKM2x2))/(MW**2*sw**2) - (3*CKM2x2*ee**2*MS**4*complexconjugate(CKM2x2))/(2.*MW**2*sw**2) + (3*CKM2x2*ee**2*MW**2*complexconjugate(CKM2x2))/sw**2)*cmath.sqrt(MC**4 - 2*MC**2*MS**2 + MS**4 - 2*MC**2*MW**2 - 2*MS**2*MW**2 + MW**4))/(48.*cmath.pi*abs(MW)**3)',
                                          (P.t,P.b__tilde__):'(((-3*CKM3x3*ee**2*MB**2*complexconjugate(CKM3x3))/(2.*sw**2) - (3*CKM3x3*ee**2*MT**2*complexconjugate(CKM3x3))/(2.*sw**2) - (3*CKM3x3*ee**2*MB**4*complexconjugate(CKM3x3))/(2.*MW**2*sw**2) + (3*CKM3x3*ee**2*MB**2*MT**2*complexconjugate(CKM3x3))/(MW**2*sw**2) - (3*CKM3x3*ee**2*MT**4*complexconjugate(CKM3x3))/(2.*MW**2*sw**2) + (3*CKM3x3*ee**2*MW**2*complexconjugate(CKM3x3))/sw**2)*cmath.sqrt(MB**4 - 2*MB**2*MT**2 + MT**4 - 2*MB**2*MW**2 - 2*MT**2*MW**2 + MW**4))/(48.*cmath.pi*abs(MW)**3)',
                                          (P.t,P.d__tilde__):'(((-3*CKM3x1*ee**2*MD**2*complexconjugate(CKM3x1))/(2.*sw**2) - (3*CKM3x1*ee**2*MT**2*complexconjugate(CKM3x1))/(2.*sw**2) - (3*CKM3x1*ee**2*MD**4*complexconjugate(CKM3x1))/(2.*MW**2*sw**2) + (3*CKM3x1*ee**2*MD**2*MT**2*complexconjugate(CKM3x1))/(MW**2*sw**2) - (3*CKM3x1*ee**2*MT**4*complexconjugate(CKM3x1))/(2.*MW**2*sw**2) + (3*CKM3x1*ee**2*MW**2*complexconjugate(CKM3x1))/sw**2)*cmath.sqrt(MD**4 - 2*MD**2*MT**2 + MT**4 - 2*MD**2*MW**2 - 2*MT**2*MW**2 + MW**4))/(48.*cmath.pi*abs(MW)**3)',
                                          (P.t,P.s__tilde__):'(((-3*CKM3x2*ee**2*MS**2*complexconjugate(CKM3x2))/(2.*sw**2) - (3*CKM3x2*ee**2*MT**2*complexconjugate(CKM3x2))/(2.*sw**2) - (3*CKM3x2*ee**2*MS**4*complexconjugate(CKM3x2))/(2.*MW**2*sw**2) + (3*CKM3x2*ee**2*MS**2*MT**2*complexconjugate(CKM3x2))/(MW**2*sw**2) - (3*CKM3x2*ee**2*MT**4*complexconjugate(CKM3x2))/(2.*MW**2*sw**2) + (3*CKM3x2*ee**2*MW**2*complexconjugate(CKM3x2))/sw**2)*cmath.sqrt(MS**4 - 2*MS**2*MT**2 + MT**4 - 2*MS**2*MW**2 - 2*MT**2*MW**2 + MW**4))/(48.*cmath.pi*abs(MW)**3)',
                                          (P.u,P.b__tilde__):'(((-3*CKM1x3*ee**2*MB**2*complexconjugate(CKM1x3))/(2.*sw**2) - (3*CKM1x3*ee**2*MU**2*complexconjugate(CKM1x3))/(2.*sw**2) - (3*CKM1x3*ee**2*MB**4*complexconjugate(CKM1x3))/(2.*MW**2*sw**2) + (3*CKM1x3*ee**2*MB**2*MU**2*complexconjugate(CKM1x3))/(MW**2*sw**2) - (3*CKM1x3*ee**2*MU**4*complexconjugate(CKM1x3))/(2.*MW**2*sw**2) + (3*CKM1x3*ee**2*MW**2*complexconjugate(CKM1x3))/sw**2)*cmath.sqrt(MB**4 - 2*MB**2*MU**2 + MU**4 - 2*MB**2*MW**2 - 2*MU**2*MW**2 + MW**4))/(48.*cmath.pi*abs(MW)**3)',
                                          (P.u,P.d__tilde__):'(((-3*CKM1x1*ee**2*MD**2*complexconjugate(CKM1x1))/(2.*sw**2) - (3*CKM1x1*ee**2*MU**2*complexconjugate(CKM1x1))/(2.*sw**2) - (3*CKM1x1*ee**2*MD**4*complexconjugate(CKM1x1))/(2.*MW**2*sw**2) + (3*CKM1x1*ee**2*MD**2*MU**2*complexconjugate(CKM1x1))/(MW**2*sw**2) - (3*CKM1x1*ee**2*MU**4*complexconjugate(CKM1x1))/(2.*MW**2*sw**2) + (3*CKM1x1*ee**2*MW**2*complexconjugate(CKM1x1))/sw**2)*cmath.sqrt(MD**4 - 2*MD**2*MU**2 + MU**4 - 2*MD**2*MW**2 - 2*MU**2*MW**2 + MW**4))/(48.*cmath.pi*abs(MW)**3)',
                                          (P.u,P.s__tilde__):'(((-3*CKM1x2*ee**2*MS**2*complexconjugate(CKM1x2))/(2.*sw**2) - (3*CKM1x2*ee**2*MU**2*complexconjugate(CKM1x2))/(2.*sw**2) - (3*CKM1x2*ee**2*MS**4*complexconjugate(CKM1x2))/(2.*MW**2*sw**2) + (3*CKM1x2*ee**2*MS**2*MU**2*complexconjugate(CKM1x2))/(MW**2*sw**2) - (3*CKM1x2*ee**2*MU**4*complexconjugate(CKM1x2))/(2.*MW**2*sw**2) + (3*CKM1x2*ee**2*MW**2*complexconjugate(CKM1x2))/sw**2)*cmath.sqrt(MS**4 - 2*MS**2*MU**2 + MU**4 - 2*MS**2*MW**2 - 2*MU**2*MW**2 + MW**4))/(48.*cmath.pi*abs(MW)**3)',
                                          (P.ve,P.e__plus__):'((-Me**2 + MW**2)*(-(ee**2*Me**2)/(2.*sw**2) - (ee**2*Me**4)/(2.*MW**2*sw**2) + (ee**2*MW**2)/sw**2))/(48.*cmath.pi*abs(MW)**3)',
                                          (P.vm,P.mu__plus__):'((-MMU**2 + MW**2)*(-(ee**2*MMU**2)/(2.*sw**2) - (ee**2*MMU**4)/(2.*MW**2*sw**2) + (ee**2*MW**2)/sw**2))/(48.*cmath.pi*abs(MW)**3)',
                                          (P.vt,P.ta__plus__):'((-MTA**2 + MW**2)*(-(ee**2*MTA**2)/(2.*sw**2) - (ee**2*MTA**4)/(2.*MW**2*sw**2) + (ee**2*MW**2)/sw**2))/(48.*cmath.pi*abs(MW)**3)'})

Decay_Z = Decay(name = 'Decay_Z',
                particle = P.Z,
                partial_widths = {(P.b,P.b__tilde__):'((-7*ee**2*MB**2 + ee**2*MZ**2 - (3*cw**2*ee**2*MB**2)/(2.*sw**2) + (3*cw**2*ee**2*MZ**2)/(2.*sw**2) - (17*ee**2*MB**2*sw**2)/(6.*cw**2) + (5*ee**2*MZ**2*sw**2)/(6.*cw**2))*cmath.sqrt(-4*MB**2*MZ**2 + MZ**4))/(48.*cmath.pi*abs(MZ)**3)',
                                  (P.c,P.c__tilde__):'((-11*ee**2*MC**2 - ee**2*MZ**2 - (3*cw**2*ee**2*MC**2)/(2.*sw**2) + (3*cw**2*ee**2*MZ**2)/(2.*sw**2) + (7*ee**2*MC**2*sw**2)/(6.*cw**2) + (17*ee**2*MZ**2*sw**2)/(6.*cw**2))*cmath.sqrt(-4*MC**2*MZ**2 + MZ**4))/(48.*cmath.pi*abs(MZ)**3)',
                                  (P.P__tilde__Chi__plus__,P.P__tilde__Chi__minus__):'(((8*ee**2*MChi**2*sw**2)/cw**2 + (4*ee**2*MZ**2*sw**2)/cw**2)*cmath.sqrt(-4*MChi**2*MZ**2 + MZ**4))/(48.*cmath.pi*abs(MZ)**3)',
                                  (P.d,P.d__tilde__):'((-7*ee**2*MD**2 + ee**2*MZ**2 - (3*cw**2*ee**2*MD**2)/(2.*sw**2) + (3*cw**2*ee**2*MZ**2)/(2.*sw**2) - (17*ee**2*MD**2*sw**2)/(6.*cw**2) + (5*ee**2*MZ**2*sw**2)/(6.*cw**2))*cmath.sqrt(-4*MD**2*MZ**2 + MZ**4))/(48.*cmath.pi*abs(MZ)**3)',
                                  (P.e__minus__,P.e__plus__):'((-5*ee**2*Me**2 - ee**2*MZ**2 - (cw**2*ee**2*Me**2)/(2.*sw**2) + (cw**2*ee**2*MZ**2)/(2.*sw**2) + (7*ee**2*Me**2*sw**2)/(2.*cw**2) + (5*ee**2*MZ**2*sw**2)/(2.*cw**2))*cmath.sqrt(-4*Me**2*MZ**2 + MZ**4))/(48.*cmath.pi*abs(MZ)**3)',
                                  (P.mu__minus__,P.mu__plus__):'((-5*ee**2*MMU**2 - ee**2*MZ**2 - (cw**2*ee**2*MMU**2)/(2.*sw**2) + (cw**2*ee**2*MZ**2)/(2.*sw**2) + (7*ee**2*MMU**2*sw**2)/(2.*cw**2) + (5*ee**2*MZ**2*sw**2)/(2.*cw**2))*cmath.sqrt(-4*MMU**2*MZ**2 + MZ**4))/(48.*cmath.pi*abs(MZ)**3)',
                                  (P.phi__minus__,P.phi__plus__):'(((-4*ee**2*Mphi**2*sw**2)/cw**2 + (ee**2*MZ**2*sw**2)/cw**2)*cmath.sqrt(-4*Mphi**2*MZ**2 + MZ**4))/(48.*cmath.pi*abs(MZ)**3)',
                                  (P.s,P.s__tilde__):'((-7*ee**2*MS**2 + ee**2*MZ**2 - (3*cw**2*ee**2*MS**2)/(2.*sw**2) + (3*cw**2*ee**2*MZ**2)/(2.*sw**2) - (17*ee**2*MS**2*sw**2)/(6.*cw**2) + (5*ee**2*MZ**2*sw**2)/(6.*cw**2))*cmath.sqrt(-4*MS**2*MZ**2 + MZ**4))/(48.*cmath.pi*abs(MZ)**3)',
                                  (P.t,P.t__tilde__):'((-11*ee**2*MT**2 - ee**2*MZ**2 - (3*cw**2*ee**2*MT**2)/(2.*sw**2) + (3*cw**2*ee**2*MZ**2)/(2.*sw**2) + (7*ee**2*MT**2*sw**2)/(6.*cw**2) + (17*ee**2*MZ**2*sw**2)/(6.*cw**2))*cmath.sqrt(-4*MT**2*MZ**2 + MZ**4))/(48.*cmath.pi*abs(MZ)**3)',
                                  (P.ta__minus__,P.ta__plus__):'((-5*ee**2*MTA**2 - ee**2*MZ**2 - (cw**2*ee**2*MTA**2)/(2.*sw**2) + (cw**2*ee**2*MZ**2)/(2.*sw**2) + (7*ee**2*MTA**2*sw**2)/(2.*cw**2) + (5*ee**2*MZ**2*sw**2)/(2.*cw**2))*cmath.sqrt(-4*MTA**2*MZ**2 + MZ**4))/(48.*cmath.pi*abs(MZ)**3)',
                                  (P.u,P.u__tilde__):'((-11*ee**2*MU**2 - ee**2*MZ**2 - (3*cw**2*ee**2*MU**2)/(2.*sw**2) + (3*cw**2*ee**2*MZ**2)/(2.*sw**2) + (7*ee**2*MU**2*sw**2)/(6.*cw**2) + (17*ee**2*MZ**2*sw**2)/(6.*cw**2))*cmath.sqrt(-4*MU**2*MZ**2 + MZ**4))/(48.*cmath.pi*abs(MZ)**3)',
                                  (P.ve,P.ve__tilde__):'(MZ**2*(ee**2*MZ**2 + (cw**2*ee**2*MZ**2)/(2.*sw**2) + (ee**2*MZ**2*sw**2)/(2.*cw**2)))/(48.*cmath.pi*abs(MZ)**3)',
                                  (P.vm,P.vm__tilde__):'(MZ**2*(ee**2*MZ**2 + (cw**2*ee**2*MZ**2)/(2.*sw**2) + (ee**2*MZ**2*sw**2)/(2.*cw**2)))/(48.*cmath.pi*abs(MZ)**3)',
                                  (P.vt,P.vt__tilde__):'(MZ**2*(ee**2*MZ**2 + (cw**2*ee**2*MZ**2)/(2.*sw**2) + (ee**2*MZ**2*sw**2)/(2.*cw**2)))/(48.*cmath.pi*abs(MZ)**3)',
                                  (P.W__minus__,P.W__plus__):'(((-12*cw**2*ee**2*MW**2)/sw**2 - (17*cw**2*ee**2*MZ**2)/sw**2 + (4*cw**2*ee**2*MZ**4)/(MW**2*sw**2) + (cw**2*ee**2*MZ**6)/(4.*MW**4*sw**2))*cmath.sqrt(-4*MW**2*MZ**2 + MZ**4))/(48.*cmath.pi*abs(MZ)**3)'})

