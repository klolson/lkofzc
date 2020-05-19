/**
 * ReviewsController
 *
 * @description :: Server-side actions for handling incoming requests.
 * @help        :: See https://sailsjs.com/docs/concepts/actions
 */

module.exports = {
    list:function(req, res){
        Reviews.find({}).exec(function(err, reviews){
            if(err){
                res.send(500, {error: 'Database Error'});
               }
            res.view('list', {reviews:reviews});
        });
    },
    add:function(req, res){
        res.view('add');
    },
    create:function(req, res){
        var code = req.body._csrf;
        var title = req.body.title;
        var body = req.body.body;
    
        Reviews.create({title:title, body:body}).exec(function(){  
            if(err){
                res.send(500, {error: 'Database Error'});
            }
        
            res.redirect('/reviews/list');
        });
    },
    view:function(req, res){
        Reviews.findOne({id:req.params.id}).exec(function(err, reviews){
           if(err){
               res.send(500, {error: 'Database Error'});
           }
            
            res.view('view', {reviews:reviews});
        });
    }
};

