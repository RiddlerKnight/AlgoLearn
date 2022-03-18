FROM alpine
RUN apk add bash
COPY ./gennerate_tree/ /home/gon/gennerate_tree
ENTRYPOINT [ "bash" ]