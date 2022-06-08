
        
def start_prog (user_id,namebot,message_in,status,message_id,name_file_picture,telefon_nome):
    import iz_func
    import iz_telegram 
    import time

    if message_in == 'Совершить взлет':
        message_out,menu,answer = iz_telegram.send_message (user_id,namebot,"Текс01",'S',0)
        time.sleep (5)
        message_out,menu,answer = iz_telegram.send_message (user_id,namebot,"Текс02",'S',0)
        time.sleep (5)
        message_out,menu,answer = iz_telegram.send_message (user_id,namebot,"Текс03",'S',0)
        time.sleep (5)
        message_out,menu,answer = iz_telegram.send_message (user_id,namebot,"Текс04",'S',0)
        time.sleep (5)
        message_out,menu,answer = iz_telegram.send_message (user_id,namebot,"Текс05",'S',0)
        

