package fm.douban.service.impl;

import fm.douban.service.SendMailService;
import org.slf4j.Logger;
import org.slf4j.LoggerFactory;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.mail.SimpleMailMessage;
import org.springframework.mail.javamail.JavaMailSender;
import org.springframework.stereotype.Service;

@Service
public class SendMailServiceImpl implements SendMailService {

    private final Logger logger = LoggerFactory.getLogger(this.getClass());

    @Autowired
    private JavaMailSender mailSender;

    public Boolean sendMail(String mail, String code){
        SimpleMailMessage message = new SimpleMailMessage();
        message.setFrom("1780934510@qq.com");
        message.setTo(mail);
        message.setSubject("验证码");
        message.setText("验证码是："+code);
        try {
            mailSender.send(message);
            return true;
        } catch (Exception e) {
            logger.error("发送邮件时发生异常了！", e);
            return false;
        }
    }
}
