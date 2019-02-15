import grpc
from concurrent import futures
import time

import image_retrival_pb2
import image_retrival_pb2_grpc

import similarImage


class SimilarImageServicer(image_retrival_pb2_grpc.SimilarImageServicer):
    def FindSimilar(self, request, context):
        if request.image is None:
            context.set_code(grpc.StatusCode.INVALID_ARGUMENT)
            context.set_details("Image is required")
            return image_retrival_pb2.ImageFileOut()
        if request.similarity not in ["Test", "CosineDistance", "EuclideanDistance"]:
            context.set_code(grpc.StatusCode.INVALID_ARGUMENT)
            context.set_details("Similarity Measure has to be one of: Test, CosineDistance, EuclideanDistance")
        response = image_retrival_pb2.ImageFileOut()
        response.imageOut1, response.imageOut2, response.imageOut3, response.imageOut4, response.imageOut5 = similarImage.find_similar(
            input_image=request.image, img_similarity=request.similarity)
        return response


class Server():
    def __init__(self):
        self.port = '[::]:50051'
        self.server = None

    def start_server(self):
        self.server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
        image_retrival_pb2_grpc.add_SimilarImageServicer_to_server(SimilarImageServicer(), self.server)
        print('Starting server. Listening on port 50051.')
        self.server.add_insecure_port(self.port)
        self.server.start()

    def stop_server(self):
        self.server.stop(0)


if __name__ == '__main__':
    server = Server()
    server.start_server()

    try:
        while True:
            time.sleep(86400)
    except KeyboardInterrupt:
        server.stop_server()
