# StreamZero FX Site ( based on Docsy )

**Please follow instructions. IMPORTANT clone with submodules as in instructions below.** 

**Please follow project management instructions further below.**

# Steps for Local Install

1. Make your own local working copy of your new repo using git clone:

```bash
git clone --recurse-submodules --depth 1 https://github.com/gridmine/site-draft.git
```
2. Change to the site-draft directory
```bash
cd site-draft
```

3. Run the image build
```bash
docker-compose build
```
4. Start the image
```bash
docker-compose up
```
5. Open http://localhost:1313 in browser

# Steps to Edit
There are 2 ways to edit.

## Option Local Edit

Following are instructions for editing locally on your desktop

1. **Before you start GIT PULL to ensure your version is up to date.**
2. Open your favorite Markdown writer ( recommend http://typora.io )
3. Browse to directory site-draft/content/en/docs ( the directory is meant for documentation but please place content here for now ) 
4. Select the suitable directory in which to place the content. If in doubt place the file in site-draft/content/en/docs/drafts
5. Write your markdown
6. Do not forget to add the yaml front mattter ( the stuff on top - check an existing page to see how )
7. Do NOT REMOVE sample pages. These are for now meant as a guide.
8. Do not edit any other settings
9. Once finished please remember to push to git. Please ensure site builds and dispays correctly before pushing to GIT.



**If you forget to pull and make changes and have issues with sync. Please follow the instructions below.** 

* rename your current directory to another name
* clone the repo as normal so you get an upto date version
* indivividually copy over the content you created into the freshly cloned directory.

## GIT Based Edit

For shorter edits and structuring it may be better to edit directly on GIT. 

* The feedback/ edit page / create child page are linked to GIT
* So you can click on the links and edit within GIT hub and make your commits directly.

# Images

Images can be placed in the directory:  site-draft/static/images/

You may also create sub-directories here for improved organisation.

These can be reffered to by using absolute links /images/......



# Project Management and Issue Reporting

* The project links to git such as feedback and create page etc are linked to the GIT Repo.
* Issue reporting: Please use the issues links to report directly into GIT.
* Where possible fix the issue yourself - not bump tasks around.
* If you are reporting an issue and have suggestions for fix please note them into the issue.

# Docsy Guide

[Docsy](https://github.com/google/docsy) is a Hugo theme for technical documentation sites, providing easy site navigation, structure, and more. This **Docsy Example Project** uses the Docsy theme, as well as providing a skeleton documentation structure for you to use. You can either copy this project and edit it with your own content, or use the theme in your projects like any other [Hugo theme](https://gohugo.io/themes/installing-and-using-themes/).

The theme is included in this project as a Git submodule:

```bash
▶ git submodule
 a053131a4ebf6a59e4e8834a42368e248d98c01d themes/docsy (heads/master)
```

This Docsy Example Project is hosted at [https://example.docsy.dev/](https://example.docsy.dev/).

You can find detailed theme instructions in the Docsy user guide: https://docsy.dev/docs/

This is not an officially supported Google product. This project is currently maintained.

## Using the Docsy Example Project as a template

A simple way to get started is to use this project as a template, which gives you a site project that is set up and ready to use. To do this: 

1. Click **Use this template**.

2. Select a name for your new project and click **Create repository from template**.

3. Make your own local working copy of your new repo using git clone:

```bash
git clone --recurse-submodules --depth 1 https://github.com/gridmine/site-draft.git
```

You can now edit your own versions of the site’s source files.

If you want to do SCSS edits and want to publish these, you need to install `PostCSS`

```bash
npm install
```

## Running the website locally

Building and running the site locally requires a recent `extended` version of [Hugo](https://gohugo.io).
You can find out more about how to install Hugo for your environment in our
[Getting started](https://www.docsy.dev/docs/getting-started/#prerequisites-and-installation) guide.

Once you've made your working copy of the site repo, from the repo root folder, run:

```
hugo server
```

## Running a container locally

You can run docsy-example inside a [Docker](https://docs.docker.com/)
container, the container runs with a volume bound to the `docsy-example`
folder. This approach doesn't require you to install any dependencies other
than [Docker Desktop](https://www.docker.com/products/docker-desktop) on
Windows and Mac, and [Docker Compose](https://docs.docker.com/compose/install/)
on Linux.

1. Build the docker image 

   ```bash
   docker-compose build
   ```

1. Run the built image

   ```bash
   docker-compose up
   ```

   > NOTE: You can run both commands at once with `docker-compose up --build`.

1. Verify that the service is working. 

   Open your web browser and type `http://localhost:1313` in your navigation bar,
   This opens a local instance of the docsy-example homepage. You can now make
   changes to the docsy example and those changes will immediately show up in your
   browser after you save.

### Cleanup

To stop Docker Compose, on your terminal window, press **Ctrl + C**. 

To remove the produced images run:

```console
docker-compose rm
```
For more information see the [Docker Compose
documentation](https://docs.docker.com/compose/gettingstarted/).

## Troubleshooting

As you run the website locally, you may run into the following error:

```
➜ hugo server

INFO 2021/01/21 21:07:55 Using config file: 
Building sites … INFO 2021/01/21 21:07:55 syncing static files to /
Built in 288 ms
Error: Error building site: TOCSS: failed to transform "scss/main.scss" (text/x-scss): resource "scss/scss/main.scss_9fadf33d895a46083cdd64396b57ef68" not found in file cache
```

This error occurs if you have not installed the extended version of Hugo.
See our [user guide](https://www.docsy.dev/docs/getting-started/) for instructions on how to install Hugo.

