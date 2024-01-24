from django.shortcuts import render
from rest_framework.decorators import action
from rest_framework.views import  APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import permissions
from .models import BlogPost
from .serializers import BlogPostSerializer
from rest_framework import viewsets

# class BlogPostViewSet(viewsets.ModelViewSet):
#     queryset = BlogPost.objects.all()
#     serializer_class = BlogPostSerializer

#     @action(detail=True,methods=['GET'])
#     def get_all_blogpost(self,request,pk=None):
#         blogpost = self.get_object()
#         return Response({'data' : blogpost})
    

class BlogPostListApiView(APIView):

    permission_classes = [permissions.IsAuthenticated]

    # get the list of blogpost

    def get(self,request,*args,**kwargs):
        blogposts = BlogPost.objects.filter(user=request.user.id)
        serializer = BlogPostSerializer(blogposts, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def post(self,request,*args,**kwargs):
        #create blogpost

        data = {
            'title': request.data.get('title'),
            'content': request.data.get('content'),
            'published_at': request.data.get('published_at'),
            'user': request.user.id
        }

        serializer =  BlogPostSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data , status=status.HTTP_201_CREATED)

        return Response(serializer.errors , status=status.HTTP_400_BAD_REQUEST )
    

class BlogPostDetailApiView(APIView):

    permission_classes = [permissions.IsAuthenticated]

    def get_blogpost(self, id,user_id):
        #use this method to fetch data 
        try:
            return BlogPost.objects.get(id=id, user=user_id)
        except BlogPost.DoesNotExist:
            return None
        
    # get one blogpost 
    def get(self,request,id,*args, **kwargs):
        blog_post_instance = self.get_blogpost(id,request.user.id)
        
        if not blog_post_instance:
            return Response(
                {
                    "message": "Object with that id does not exist"},
                    status=status.HTTP_400_BAD_REQUEST   
            )
        
        serializer = BlogPostSerializer(blog_post_instance)
        return  Response(serializer.data, status=status.HTTP_200_OK)
    
    # update a blogpost 
    def put(self, request,id,*args,**kwargs):
        blog_instance = self.get_blogpost(id, request.user.id)

        if not blog_instance:
            return Response(
                {"message": "Blog post not found "},
                status = status.HTTP_400_BAD_REQUEST
            )
        
        data = {
            'title': request.data.get('title'),
            'content': request.data.get('content'),
            'published_at': request.data.get('published_at'),
            'user': request.user.id
        }

        serializer = BlogPostSerializer(instance=blog_instance, data=data,partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    # Request to delete a blogpost 
    def delete(self,request,id,*args,**kwargs):

        blog_instance = self.get_blogpost(id, request.user.id)

        if not blog_instance:
            return Response(
                {'message': "Blogpost not found"},
                status= status.HTTP_404_NOT_FOUND
            )
        
        blog_instance.delete()
        return Response( 
            {'message':'Blogpost deleted'}, status=status.HTTP_200_OK
        )
