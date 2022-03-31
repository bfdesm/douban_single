package fm.douban.app.api;

import fm.douban.model.Comment;
import fm.douban.model.Result;
import fm.douban.service.CommentService;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Controller;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.RequestParam;
import org.springframework.web.bind.annotation.ResponseBody;

import javax.servlet.http.HttpServletRequest;
import java.util.List;

/**
 * @author zeyu
 */
@Controller
public class CommentAPI {

    @Autowired
    private CommentService commentService;

    @PostMapping("/api/comment/post")
    @ResponseBody
    public Result<Comment> post(@RequestParam("refId") String refId, @RequestParam(value = "parentId") Long parentId,
                                @RequestParam("content") String content, HttpServletRequest request) {
        long userId = (long) request.getSession().getAttribute("userId");
        return commentService.post(refId, userId, parentId, content);
    }

    @GetMapping("/api/comment/query")
    @ResponseBody
    public Result<List<Comment>> query(@RequestParam("refId") String refId) {
        return commentService.query(refId);
    }
}
