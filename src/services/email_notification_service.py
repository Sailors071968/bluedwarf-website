MTP"("s"e
lEfm.asimlt pN_osteirfviecra,t isoenl fS.esrmvtipc_ep ofrotr) 
B l u e D w a r f 
 S e nsdesr v1e0r,. s7t,a ratntdl s3(-)d
a y   s u b s c r i p t isoenr vreerm.ilnodgeirns(
  s"e"l"f
.
  siemnpdoerrt_ esmmatipll,i bs
eflrfo.ms eenmdaeirl_.pmaismsew.otredx)t
  i m p o r t   M I M E Tteexxtt
 f=r omms gd.aatse_tsitmrei nigm(p)o
r t   d a t e t i m e 

scelravsesr .EsmeanidlmNaoitli(fsieclaft.isoennSdeerrv_iecmea:i
l ,   r edceifp i_e_nitn_ietm_a_i(ls,e ltfe)x:t
) 
              s e l f . ssmetrpv_esre.rqvueirt (=) 
" s m t p . g m a i l . c
o m " 
                 sleolgfg.isnegn.dienrf_oe(mfa"iElm a=i l" nsoetnitf iscuactcieosnssf@ubllluye dtwoa r{fr.eicoi"p
                 i e n t _ e m a i
                 l } " ) 
                 d e f   s e n d _ s u b srcertiuprtni oTnr_uree
                 m i n d e r ( s e l f ,  
                 u s e r _ e m a ielx,c eupste rE_xncaempet,i ozni pa_sc oed:e
                 ,   d a y s _ u n t i l _lboiglgliinngg.,e rnreoxrt(_fb"iFlaliilnegd_ dtaot es)e:n
                 d   e m a i l :  "{"s"tSre(ned) }s"u)b
                 s c r i p t i o n   r e mrientduerrn  eFmaalisle"""
                         subject = f"BlueDwarf Subscription Reminder - {days_until_billing} Days Until Billing"

                                         if days_until_billing == 10:
                                                     body = f"Dear {user_name}, Your BlueDwarf subscription for zip code {zip_code} will be renewed in 10 days. Your credit card will be charged $49.00 on {next_billing_date}."
                                                             elif days_until_billing == 7:
                                                                         body = f"Dear {user_name}, Your BlueDwarf subscription for zip code {zip_code} will be renewed in 7 days. Your credit card will be charged $49.00 on {next_billing_date}."
                                                                                 elif days_until_billing == 3:
                                                                                             body = f"Dear {user_name}, FINAL REMINDER: Your BlueDwarf subscription for zip code {zip_code} will be renewed in 3 days. Your credit card will be charged $49.00 on {next_billing_date}."
                                                                                                     
                                                                                                             return self._send_email(user_email, subject, body)
                                                                                                                 
                                                                                                                     def _send_email(self, recipient_email, subject, body):
                                                                                                                             """Send email using SMTP"""
                                                                                                                                     try:
                                                                                                                                                 msg = MIMEText(body)
                                                                                                                                                             msg['Subject'] = subject
                                                                                                                                                                         msg['From'] = self.sender_email
                                                                                                                                                                                     msg['To'] = recipient_email
                                                                                                                                                                                                 
                                                                                                                                                                                                             # Email sending logic here
                                                                                                                                                                                                                         return True
                                                                                                                                                                                                                                 except Exception as e:
                                                                                                                                                                                                                                             return False
